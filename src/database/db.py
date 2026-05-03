import streamlit as st
from src.database.config import supabase
from datetime import datetime
import bcrypt
def hashed(password):
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
def check_password(password,hashed):
    return bcrypt.checkpw(password.encode(),hashed.encode())

def teacher_username_exist(user_name):
    response=supabase.table("teacher").select("user_name").eq("user_name",user_name).execute()
    if len(response.data) > 0:
        return True
    return False
def add_teacher_profile(user_name,name,password):
    data={"user_name":user_name,"name":name,"password":hashed(password)}
    response=supabase.table("teacher").insert(data).execute()
    return response.data
def login(user_name,password):
    if "teacher_id" not in st.session_state:
        st.session_state["teacher_id"]=None
    try:

      response=supabase.table("teacher").select("*").eq("user_name",user_name).execute()
      
      teacher_table_info=response.data[0]
    except:
        st.error("user name not found")
    
    if response.data:
        teacher=response.data[0]
        if check_password(password,teacher["password"]):
            st.session_state["teacher_id"]=teacher_table_info["teacher_id"]
            return teacher
    return None
def get_all_students():
    response=supabase.table("student").select("*").execute()
    return response.data
def create_student_profile(new_name,face_embedding,voice_emb):
    data={"name":new_name,"face_embedding":face_embedding,"voice_embedding":voice_emb}
    response=supabase.table("student").insert(data).execute()
    return response
def crate_new_subject(code,name,section,teacher_id):
    data={"subject_code":code,"subject_name":name,"section":section,"teacher_id":teacher_id}
    response=supabase.table("subject").insert(data).execute()
    return response.data
def get_teacher_subject(teacher_id):
    response=supabase.table("subject").select("*,student_subject(count)","attendance_log(*)").eq("teacher_id",teacher_id).execute()
    subjects=response.data
    for sub in subjects:
        sub["total_student_per_subject"]=sub.get("student_subject",[{}])[0].get("count",0) if sub.get("student_subject") else 0
        attendance=sub.get("attendance_log")
        unique_sessions=len(set(log["timestamp"] for log in attendance))
        total_classes=unique_sessions
        sub["total_classes"]=total_classes
        sub.pop("student_subject",None)
        sub.pop("attendance_log",None)
    if subjects:
     return subjects
    return None
def enrol_student_to_subject(student_id,subject_id):
    data={"student_id":student_id,"subject_id":subject_id}
    response=supabase.table("student_subject").insert(data).execute()
    return response.data
def unenrol_student_to_subject(student_id,subject_id):
    response=supabase.table("student_subject").delete().eq("student_id",student_id).eq("subject_id",subject_id).execute()
    return response.data
def get_student_subject(student_id):
    response=supabase.table("student_subject").select("*,subject(*)").eq("student_id",student_id).execute()
    return response.data
def get_student_attendance(student_id):
    response=supabase.table("attendance_log").select("*,subject(*)").eq("student_id",student_id).execute()
    return response.data
def add_attendance(records):
    response=supabase.table("attendance_log").insert(records).execute()
    return response.data
def get_attendance_for_teacher(teacher_id):
    
    response = supabase.table('attendance_log') .select("*, subject!inner(*)") .eq('subject.teacher_id', teacher_id).execute()
    return response.data

    
    

    