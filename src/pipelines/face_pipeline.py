import streamlit as st
import numpy as np
from deepface import DeepFace
from src.database.db import get_all_students

@st.cache_resource
def load_model():
    return DeepFace.build_model("Facenet")

def get_face_embeddings(photo_np):
    try:
        load_model()
        result = DeepFace.represent(
            img_path=photo_np,
            model_name="Facenet",
            enforce_detection=True,
            detector_backend="opencv"
        )
        return [np.array(r["embedding"]) for r in result]
    except Exception:
        return []

def student_classifier():
    students_db = get_all_students()
    if not students_db:
        return None
    images, ids = [], []
    for student in students_db:
        face = student.get("face_embedding")
        student_id = student.get("student_id")
        if not face or not student_id:
            continue
        images.append(np.array(face))
        ids.append(student_id)
    if not ids:
        return None
    if len(set(ids)) < 2:
        return {"images": images, "ids": ids}
    from sklearn.svm import SVC
    classifier = SVC(kernel="linear", class_weight="balanced", probability=True)
    classifier.fit(images, ids)
    return {"classifier": classifier, "images": images, "ids": ids}

def train_classifier():
    st.cache_resource.clear()
    return bool(student_classifier())

def attendance_prediction(photo_np):
    face_embeddings = get_face_embeddings(photo_np)
    detected_students = {}
    model_data = student_classifier()
    if not model_data:
        return None, [], len(face_embeddings)
    images = model_data["images"]
    ids = model_data["ids"]
    all_students = sorted(list(set(ids)))
    for face_embedding in face_embeddings:
        if len(all_students) == 1:
            detected_students[all_students[0]] = True
            break
        classifier = model_data["classifier"]
        predicted_id = int(classifier.predict([face_embedding])[0])
        student_embeddings = [e for e, i in zip(images, ids) if i == predicted_id]
        distances = [np.linalg.norm(e - face_embedding) for e in student_embeddings]
        if not distances:
            continue
        if min(distances) <=10:
            detected_students[predicted_id] = True
    return detected_students, all_students, len(face_embeddings)