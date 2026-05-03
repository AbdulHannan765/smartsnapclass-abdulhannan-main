import streamlit as st
from src.database.config import supabase
from src.database.db import enrol_student_to_subject,unenrol_student_to_subject,get_student_subject,get_student_attendance

@st.dialog("enrol for subject")
def enrol():
    student_id=st.session_state["student_id"]

    st.subheader("Enrol")
    st.write("Enter the subject code provided by your faculty")
    

    join_code=st.text_input("subject code",placeholder="eg : CS19....")
    if st.button("enrol"):
        if join_code:
            res=supabase.table("subject").select("subject_id,subject_name,subject_code").eq("subject_code",join_code).execute()
            if res.data:
                subject=res.data[0]
                
                response=supabase.table("student_subject").select("*").eq("student_id",student_id).eq("subject_id",subject["subject_id"]).execute()
                if response.data:
                    st.error("you are already enroled")
                else:
                    enrol_student_to_subject(student_id,subject["subject_id"])
                    st.success("you have enroled succesfully")
                    st.rerun()
                    
            else:

                st.error("subject code not found")
        else:
            st.error("please enter subject code")
def show_enroled_subjects():
    student_id = st.session_state["student_id"]

    with st.spinner("Your subjects are loading..."):
        subjects = get_student_subject(student_id)
        logs = get_student_attendance(student_id)

    # 🔹 Build stats per subject
    stats = {}

    for log in logs:
        subject_id = log["subject_id"]

        if subject_id not in stats:
            stats[subject_id] = {"total": 0, "attended": 0}

        stats[subject_id]["total"] += 1

        if log.get("is_present"):
            stats[subject_id]["attended"] += 1

    # 🔹 Display subjects
    for sub_i in subjects:
        subject_id = sub_i["subject_id"]
        subject_name = sub_i["subject"]["subject_name"]
        sub_stats = stats.get(subject_id, {"total": 0, "attended": 0})
        with st.container(border=True):

            st.subheader(subject_name)


            st.write(f"Subject Code: {sub_i['subject']['subject_code']}")
            st.write(f"Section: {sub_i['subject']['section']}")


            st.write(f"Total Classes: {sub_stats['total']}")
            st.write(f"Attended: {sub_stats['attended']}")

        # 🔹 Unenrol button
        if st.button(f"Unenrol {subject_name}", key=f"unenrol_{subject_id}"):
            unenrol_student_to_subject(student_id, subject_id)
            st.success("Unenrolled successfully")
            st.rerun()