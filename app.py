import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_dash_board import student_dashboard
from src.screens.faculty_dashboard import teacher_dashboard
from src.components.auto_enrol import auto_enrol_dialog

def main():
   st.set_page_config(
       page_title="SnapClass - Smart Attendance Marking by AI",
       page_icon="https://cdn-icons-png.flaticon.com/512/3135/3135755.png"
   )

   if "login_type" not in st.session_state:

      st.session_state["login_type"]=None
   join_code=st.query_params.get("join_code")
   if join_code:
       if st.session_state["login_type"]!="student":
           st.session_state["login_type"]="student"
           
       if st.session_state["login_type"]=="student" and "student_id" in st.session_state:
           auto_enrol_dialog(join_code)
           st.rerun()
   match st.session_state["login_type"]:
         case "teacher":
            teacher_screen()
         case "student":
            student_screen()
       
         case None:
            home_screen()

   
           
   

main()
      
    


