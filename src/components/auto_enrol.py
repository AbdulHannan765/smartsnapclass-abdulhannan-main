import streamlit as st
from src.database.config import supabase
from src.database.db import enrol_student_to_subject
@st.dialog("auto enrol")
def auto_enrol_dialog(subject_code):
   
    student_id=st.session_state["student_id"]
    response=supabase.table("subject").select("subject_id","subject_name").eq("subject_code",subject_code).execute()
    subject=response.data[0] if response.data else None

    if not response.data:
        st.error("subject not found")
        if st.button("close"):
            st.query_params.clear()
            st.rerun()
        return
    check=supabase.table("student_subject").select("*").eq("student_id",student_id).eq("subject_id",subject["subject_id"]).execute()
    if check.data:
            st.warning("you have alredy enroled to this subject")
            if st.button("close"):
                st.query_params.clear()
                st.rerun()
                return
    st.markdown(f"dou want to enrol to {subject['subject_name']}")
    col1,col2=st.columns(2)
    with col1:
        if st.button("YES"):
            if enrol_student_to_subject(student_id,subject["subject_id"]):
                st.success("you have enroled succesfully")
                st.query_params.clear()
                st.rerun()
    with col2:
        if st.button("NO"):
            st.query_params.clear()
            st.rerun()



