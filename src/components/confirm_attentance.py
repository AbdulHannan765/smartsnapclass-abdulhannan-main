import streamlit as st
from src.database.db import add_attendance
import time
@st.dialog("confirm attendance")
def confirm_attendance_dialog(dic,show):
   
    
    st.dataframe(show,hide_index=True)

    col1,col2=st.columns(2)
    with col1:
     if st.button("confirm "):
        add_attendance(dic)
       
        st.info("conformed")
        time.sleep(2)
        st.rerun()
    with col2:
      if st.button("cancel"):
          
          st.info("cancelled")
          time.sleep(2)
          st.rerun()
          
          