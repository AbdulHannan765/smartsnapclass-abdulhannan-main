import streamlit as st

from src.ui.base_layout import   hide_streamlit_layout
from src.ui.base_layout import  home_font_and_style
from src.ui.base_layout import style_backround_home
from src.screens.faculty_tabs import attendance_records,take_attendance,manage_subjects
def teacher_dashboard():
   
    if "current_faculty_tab" not in st.session_state:
        st.session_state["current_faculty_tab"]="take_attendance"
   
         
         
         

    
    style_backround_home()
    hide_streamlit_layout()
    home_font_and_style()
    
    col1,col2=st.columns(2)
    with col1:
        st.markdown("""
            <div style="text-align: center; margin-top: -20px;">
                <img src="https://cdn-icons-png.flaticon.com/512/3135/3135755.png" width="180">
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
    with col2:
         
        if st.button("Log Out",type="tertiary"):
           st.session_state.clear()
           st.rerun()
    tab1,tab2,tab3=st.columns(3)
    with tab1:
        if st.session_state["current_faculty_tab"]=="take_attendance":
            type="tertiary"
        else:
            type="primary"

        if st.button("Take Attendance",type=type):
            st.session_state["current_faculty_tab"]="take_attendance"
            st.rerun()
            
            
            
    with tab2:
        if st.session_state["current_faculty_tab"]=="manage_subjects":
              type="tertiary"
        else:
            type="primary"
        if st.button("Manage Sybjects",type=type):
               st.session_state["current_faculty_tab"]="manage_subjects"
               st.rerun()
               
            
               
    with tab3:
        if st.session_state["current_faculty_tab"]=="attendance_record":
              type="tertiary"
              
        else:
            type="primary"
        if st.button("Attendance_Record",type=type):
               st.session_state["current_faculty_tab"]="attendance_record"
               st.rerun()
    st.space()
             
            
    if  st.session_state["current_faculty_tab"]=="take_attendance":
         take_attendance()
    elif st.session_state["current_faculty_tab"]=="manage_subjects":
         manage_subjects()
    else:
         attendance_records()





    