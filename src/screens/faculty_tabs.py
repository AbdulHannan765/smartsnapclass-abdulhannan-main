import streamlit as st
from src.database.db import crate_new_subject,get_teacher_subject,add_attendance,get_student_attendance
from src.screens.join import share_subject
from PIL import Image
from src.components.add_photo import add_photos_dialogue

from src.pipelines.face_pipeline import attendance_prediction
from src.database.config import supabase
from datetime import datetime
import numpy as np
import time
from src.components.confirm_attentance import confirm_attendance_dialog 

from src.database.db import get_attendance_for_teacher


import pandas as pd
def take_attendance():
   st.header('Take Attendance')
   present_student_ids=set()
   teacher_id=st.session_state["teacher_id"]
   
   records = []
   show=[]
   student_ids=set()
   subjects=get_teacher_subject(teacher_id)
  
   if "attendance_images" not in st.session_state:
       st.session_state["attendance_images"]=[]
   if not subjects:
       st.error("no subject found please create a subject first")
       return
   subject_options={f"{s['subject_name']}-{s['section']}":s['subject_id'] for s in subjects}
   col1,col2=st.columns([3,1])
   with col1:
    selected_subject=st.selectbox("select subject to take attenfdance",options=list(subject_options.keys()))
   with col2:
       if st.button("add photo"):
          
           add_photos_dialogue()
       subject =subject_options[selected_subject]
       subject_name=supabase.table("subject").select("subject_name").eq("subject_id",subject).execute().data[0]["subject_name"]
   st.divider()
   images=st.session_state["attendance_images"]
   image_cols=st.columns(3)
   for index,image in enumerate(images):
       with image_cols[index%3]:
         st.image(image)

   col1,col2=st.columns(2)
   with col1:
       if st.button("clear photos"):
           st.session_state["attendance_images"]=[]
           st.rerun()
   with col2:
    
       
    has_images=bool(st.session_state["attendance_images"])
    all_enrolled_stu = supabase.table("student_subject").select("*").eq("subject_id", subject).execute().data
    

    enroled_students = {}
   
    if all_enrolled_stu:
    
        all_enrolled_stu_ids = [stu["student_id"] for stu in all_enrolled_stu]

        
        student_name = supabase.table("student").select("name,student_id").in_("student_id", all_enrolled_stu_ids).execute().data
    else:
        st.error("no student have enroled yet for this subject")
        return
   
    for stu in student_name:
        enroled_students[stu["student_id"]] = stu["name"]
    if st.button("run face analysis"):      
        if has_images:
            
                for image in st.session_state["attendance_images"] :
                    image=np.array(image)
                    detected,_,_=attendance_prediction(image)
                    if not detected:
                        st.warning("no student detected in one of the photos")
                    if detected:
                        with st.spinner("analyzing photos ...."):
                            time.sleep(2)
                            for sid in detected.keys():
                                 student_ids.add(int(sid))
               

                        
                timestamp=datetime.now().isoformat()
                        
                for student in all_enrolled_stu:
                                if student["student_id"] in student_ids:
                                    
                                    if student["student_id"]  not in present_student_ids:
                                        name=enroled_students[student["student_id"]]
                                        records.append({
                                            "timestamp": timestamp,
                                            "student_id": student["student_id"],
                                            "subject_id": subject,
                                            
                                            "is_present": True
                                            
                                        })
                                        show.append({
                                            "timestamp": datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %I:%M %p") if timestamp else "N'A",
                                            
                                            "student_id": student["student_id"],
                                            "name":name,
                                            
                                            
                                            "subject_name":subject_name,
                                            
                                            "present": "Present ✅"
                                        })
                                    present_student_ids.add(student["student_id"])
                                elif student["student_id"] not in student_ids:
                                    name=enroled_students[student["student_id"]]
                                    if student["student_id"]  not in present_student_ids:
                                        records.append({
                                                "timestamp": timestamp,
                                                "student_id": student["student_id"],
                                                "subject_id": subject,
                                                
                                                "is_present": False
                                            
                                            })
                                        show.append({
                                                "timestamp": datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %I:%M %p") if timestamp else "N'A",

                                                "student_id": student["student_id"],
                                                
                                                "name": name,
                                                "subject_name":subject_name,
                                            
                                                "present": "Absent ❌"
                                            })
                                        present_student_ids.add(student["student_id"])
                                            
                                        
            
            
        
                confirm_attendance_dialog(records,show)
        else:
            st.error("please add photos to take attendance")
            st.rerun()





                            

                
                            

                   
   
       
    

@st.dialog("create new subject")
def create_sub_dialogue(teacher_id):
    
           name=st.text_input("enter the Subject Name")
           code=st.text_input("enter the Subject Code")
           section=st.text_input("enter the Section")
           if st.button("create_subject"):
            if name and code and section :

                try:
                    crate_new_subject(code,name,section,teacher_id)
                    
                except Exception as e:
                    st.error("cant create subject de=ue to unknown error")
            else:
                st.info("please fill all requirements")
        
def tablet(subject_name,subject_code,total_classes,total_students,sec,teacher_id):
   
    with st.container(border=True):
       
        st.write(f"Subject Name : {subject_name}")
        col1,col2=st.columns(2)
        with col1:
            st.write(f"Subject Code : {subject_code}")
            st.space()
            st.write(f"Students : {total_students}")
        with col2:
            st.write(f"Section : {sec}")
            st.space()
            st.write(f"Classes : {total_classes}")
        
            
        
def manage_subjects():
   teacher_id=st.session_state["teacher_id"]
   col1,col2=st.columns(2)
   with col1:
            st.write("manage subjects")
   with col2:
         if st.button("Create New Subject"):
            create_sub_dialogue(teacher_id)
   
   
   subjects=get_teacher_subject(teacher_id)
   subject_name="Not yet added"
   subject_code="Not yet added"
   sec="Not yet added"
   total_classes=0
   total_students=0


   if subjects:
    for sub in subjects:
        total_classes=sub["total_classes"]
        if sub["total_student_per_subject"]:
         total_students=sub["total_student_per_subject"]
        else:
            total_students=0

        sec=sub["section"]
        subject_name=sub["subject_name"]
        subject_code=sub["subject_code"]
        
        tablet(subject_name,subject_code,total_classes,total_students,sec,teacher_id)
        
        
        
        if subject_name!="Not yet added" and  subject_code!="Not yet added" and  sec!="Not yet added":
  
         if  st.button(f"share code of {subject_name}",key=f"share_{subject_code}",icon=":material/share:"):
                share_subject(subject_name,subject_code)
        
        st.space()
   else:
        st.error("no subject found")
    
        

           
        
            


def attendance_records():
    st.header("attendance_records")
    teacher_id=st.session_state["teacher_id"]
    records=get_attendance_for_teacher(teacher_id)
    data=[]
    for re in records:
        ts=re.get("timestamp")
        data.append({
            "ts_group": ts.split(".")[0][:13],
            "time":datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N'A",
            "subject":re["subject"]["subject_name"],

            "subject_code":re["subject"]["subject_code"],
            "present":bool(re.get("is_present",False)),
        })
    df=pd.DataFrame(data)
    summary=(
        df.groupby(["ts_group","time","subject","subject_code"]).agg(present=("present","sum"),total=("present","count")).reset_index()
    )
    summary["Attendance"]=("✅ "+summary['present'].astype(str)+"/"+summary['total'].astype(str)+"Students")
    display_df=(summary.sort_values(by="ts_group",ascending=False)
                [["time","subject","subject_code","Attendance"]])
    st.dataframe(display_df,hide_index=True)
