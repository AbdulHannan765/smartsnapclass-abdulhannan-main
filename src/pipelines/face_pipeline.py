import streamlit as st
from sklearn.svm import SVC
import dlib
import face_recognition_models
import numpy as np
from src.database.db import get_all_students
def load_dlib_models():
    detector=dlib.get_frontal_face_detector()
    shape_predictor=dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )
    face_rec=dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )
    return detector,shape_predictor,face_rec
def get_face_embeddings(photo_np):
    detector,shape_predictor,face_rec=load_dlib_models()
    faces=detector(photo_np,1)
    embeddings=[]
    for face in faces:
        land_marks=shape_predictor(photo_np, face)
        face_discriptor=face_rec.compute_face_descriptor(photo_np, land_marks, 1)
        embeddings.append(np.array(face_discriptor))
    return embeddings

def student_classifier():
    images=[]
    ids=[]
    students_db=get_all_students()
    if not students_db:
        return None
    for student in students_db:
        if not student:
            return None
        face=student.get("face_embedding")
        student_id=student.get("student_id")
        if not student_id :
            return None
        images.append(np.array(face))
        ids.append(student_id)
    classifier=SVC(kernel="linear",class_weight="balanced",probability= True)
    try:
        classifier.fit(images,ids)
    except ValueError:
        st.info("hmmmmmmmm")
        
    return {"classifier":classifier,"images":images,"ids":ids}
def train_classifier():
    st.cache_resource.clear()
    model_data=student_classifier()
    return bool(model_data)
def attendance_prediction(photo_np):
    face_embeddings=get_face_embeddings(photo_np)
    detected_students={}
    model_data_and_learning=student_classifier()
    if not model_data_and_learning:
        return None,[],len(face_embeddings)
    classifier=model_data_and_learning["classifier"]
    images=model_data_and_learning["images"]
    ids=model_data_and_learning["ids"]
    all_students=sorted(list(set(ids)))
    for face_embedding in face_embeddings:
        if len(all_students)>1:

            predicted_id=int(classifier.predict([face_embedding])[0])
        else:
            id_A=all_students[0]
            detected_students[id_A]=True
            return detected_students,all_students,len(face_embeddings)
        student_embeddings = [
        emb for emb, id_ in zip(images, ids)
        if id_ == predicted_id
        ]

        distances = [
            np.linalg.norm(e - face_embedding)
            for e in student_embeddings
        ]
        threshold=0.5
        if not distances:
           continue
 
        best_match_score = min(distances)
        if best_match_score<=threshold:
            detected_students[predicted_id]=True
        else:
            continue
    return detected_students,all_students,len(face_embeddings)
    



    
