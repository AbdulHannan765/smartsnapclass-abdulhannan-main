import streamlit as st
from src.ui.base_layout import login_background_student,hide_streamlit_layout,home_font_and_style
import numpy as np
from PIL import Image
from src.pipelines.face_pipeline import attendance_prediction,get_face_embeddings,train_classifier

from src.database.db import get_all_students,create_student_profile
from src.screens.student_dash_board import student_dashboard
from src.screens.home_screen import home_screen
import time 
from src.database.config import supabase
def student_screen():
   if "student_data" in st.session_state and st.session_state["student_data"]!=None and "student_id" in st.session_state and st.session_state["student_id"]!=None:
      
      student_dashboard()
      
      return
   
   
   
  

   if st.button("home",type="tertiary",width=250,key="1265to_home"):
      st.session_state.clear()
      st.rerun()
   
   login_background_student()
   hide_streamlit_layout()
   home_font_and_style()
   st.header("Student Screen")
   photo_source=st.camera_input("enter your photo")
   res_c = supabase.table("student").select("*", count="exact").execute()
   total_students = res_c.count or 0


   if photo_source:
      image=np.array(Image.open(photo_source))
      with st.spinner("AI is scanning"):
         detected_student_ids,all_student_ids,no_of_students=attendance_prediction(image)
         if no_of_students==0:
            st.error("student not  found")
         elif no_of_students>1:
            st.error("multiple students   found")
         else:
         
           
            if detected_student_ids and total_students>1  : #total_students>1
                  student_id = list(detected_student_ids.keys())[0]
                  all_students = get_all_students()

                  for student_info in all_students:
                     if student_info.get("student_id") == student_id:
                           s_name=student_info.get("name")
                          
                           st.session_state["login_type"] = "student"
                           
                           st.session_state["student_data"]=student_info
                           st.session_state["student_id"]=student_id
                           
                           
                           st.toast("Welcome")
                           st.info(f"{no_of_students} of students found")
                           st.write(f"{s_name} your profile is already registered")
                           time.sleep(3)
                           
                           st.rerun()
                           
                          

                           
                          
                           
                        



            else:
               
                  st.info("you might be a new student registor first")
                 
                  
                  
                  with st.container(border=True):
                        st.header("Registor new profile")
                        new_name=st.text_input("enter your name")

            
                        audio_data=None
                      
                       
                        if st.button("registor"):
                           if not new_name or  image is None:
                              st.error("you dint  entered your name or photo")
                           else:
                              with st.spinner("adding your profile"):
                                 face_embedding=get_face_embeddings(image)

                                 
                                 if face_embedding:
                                    face_embedding=face_embedding[0].tolist()
                                    voice_emb=None
                                    
                                    response=create_student_profile(new_name,face_embedding,voice_emb)
                                    if response.data:
                                       train_classifier()
                                       st.session_state["login_type"]="student"
                                       st.session_state["student_data"]=response.data
                                       
                                       
                                      
                                       st.toast(f"your profile is creted {new_name}")
                                       time.sleep(3)
                                       
                                    
                                       st.rerun()
                                       
                                 else:
                                    st.error("coudent extract facial features")
   
                                          
                                    
                                 
                                 










