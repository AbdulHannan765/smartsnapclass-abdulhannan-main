import streamlit as st
from src.ui.base_layout import login_background_student,hide_streamlit_layout,home_font_and_style
from src.components.dialog_enrol import show_enroled_subjects,enrol

def student_dashboard():
   login_background_student()
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
   st.divider()
   with col2:
      
      if st.button("Log Out",type="tertiary"):
         st.session_state.clear()
         
         st.rerun()
   st.space()
   col11,col12=st.columns(2)
   with col11:
      st.write("your enroled subject")
      show_enroled_subjects()
   with col12:
      if st.button("enrol to subject"):
       enrol()
      
   
    


