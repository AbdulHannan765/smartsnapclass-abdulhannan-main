
import streamlit as st
from src.ui.base_layout import login_background_teacher
from src.ui.base_layout import   hide_streamlit_layout
from src.ui.base_layout import  home_font_and_style
from src.screens.home_screen import home_screen
from src.database.db import teacher_username_exist,add_teacher_profile,login
from src.screens.faculty_dashboard import teacher_dashboard
def teacher_screen():
    if "allow_teacher_dashboard"  in st.session_state and st.session_state["allow_teacher_dashboard"]=="allow":
     teacher_dashboard()
     return
    else:
   
            home_font_and_style()
            hide_streamlit_layout()
            login_background_teacher()
            if st.button("BACK TO HOME" ,type="tertiary",width=250,key="1265to_home"):
                  st.session_state.clear()
                  
                  st.rerun()
            
            
                  

                  
            if "faculty_login_type" not in st.session_state or st.session_state["faculty_login_type"]=="login" or st.session_state["faculty_login_type"]==None:
                        faculty_login()
            elif st.session_state.faculty_login_type=="Registor":
                        faculty_registration()
                  
                        
                  

def registration(username,name,password,confirm_password):
      if not username or not name or not password or not confirm_password:
            return False,"fill all the columns"
      if password!=confirm_password:
            return False,"confirm your password correctly"
      if teacher_username_exist(username):
            return False,"user name already exist ,chose another username"
      if password!=confirm_password:
            return False,"confirm your password correctly"
      try:   
         add_teacher_profile(username,name,password)
         return True,"your profile has been succesfully registered"
      except Exception as e:
            return False,"unexpected error"
            

def  faculty_login():
    st.session_state["faculty_login_type"]="login"
    st.header("FACULTY Login")
    username=st.text_input("Enter UserName")
    password=st.text_input("Enter your password",type="password",key="login_pass")


    col1,col2=st.columns(2)
    with col1:
            if st.button("Login",type="primary",width=200,key="1"):
                  if login(username,password):
                        st.toast("welcome !")
                        st.session_state["login_type"]="teacher"
                        st.session_state["allow_teacher_dashboard"]="allow"
                
                        import time
                        time.sleep(1)
                        st.rerun()

                  else:
                        st.error("invalid username or password")

    with col2:
            if st.button("Registor instead",type="secondary",width=200,key="2"):
                 
                 st.session_state["faculty_login_type"]="Registor"
                 st.rerun()
                 
                  
     
def faculty_registration():
      
        
        
        st.header("FACULTY REGISTRATION")
        username=st.text_input("Enter UserName",key="registration_user_name")
        name=st.text_input("Enter Name",key="name")
        password=st.text_input("Set your password",type="password",key="reg_set_pass")
        confirm_password=st.text_input("Confirm your password",type="password")
        
        
        
        col1,col2=st.columns(2)
        with col1:
                if st.button("Registor",type="primary",width=200,key="s11"):
                      success,message=registration(username,name,password,confirm_password)
                      if success:
                            st.success(message)
                            import time
                            time.sleep(3)
                            st.session_state["faculty_login_type"]="login"
                            st.rerun()
                      else:
                            st.error(message)
        with col2:
                if st.button("Login instead",type="secondary",width=200,key="u12"):
                      
                      st.session_state["faculty_login_type"]="login"
                      
                      st.rerun()
                     
                      
                    

                  


   
    
    

        