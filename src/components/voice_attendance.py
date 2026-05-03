# import streamlit as st
# from src.database.config import supabase
# from src.pipelines.voice_pipeline import process_bulk_voice
# from datetime import datetime
# from src.components.confirm_attentance import confirm_attendance_dialog
 
# @st.dialog("voice attendance")
# def voice_attendance_dialog(subject_id):
#     st.write("Enter voice of all students in once to take attendance")
#     records=[]
#     show=[]
#     audio=None

#     audio=st.audio_input("enter bulk audio")
#     present_student_ids=set()
#     timestamp=datetime.now().isoformat()
#     if st.button("take attendance"):
#         if audio:
#             with st.spinner("AI is analyzing the audio"):
#                 enroled_res=supabase.table("student_subject").select("*,student(*),subject(*)").eq("subject_id",subject_id).execute()
#                 enroled_students=enroled_res.data
#                 id_name_map={stu["student_id"]: stu["student"]["name"] for stu in enroled_students}
#                 subject_id_name_map={stu["subject_id"]: stu["subject"]["subject_name"] for stu in enroled_students}

#                 if not enroled_students:
#                     st.warning("no students enroled for this subject")
#                     return
#                 all_students_with_audio={}
                
#                 for stu in enroled_students:
#                     if stu["student"]["voice_embedding"]:
#                        all_students_with_audio[stu["student"]["student_id"]]=stu["student"]["voice_embedding"]
#                 if not all_students_with_audio:
#                     st.warning("no student has registered voice data")
#                     return
#                 audio_bytes=audio.read()
#                 detected_scores=process_bulk_voice(audio_bytes, all_students_with_audio)
#                 if not detected_scores.keys():
#                     st.warning("no student detected in the audio")
#                     return  
#                 for one in all_students_with_audio:
#                     id=one
#                     score=detected_scores.get(id,0.0)

#                     if score>0.0:
#                           is_present=True
#                     else:
#                             is_present=False
                        
                    
                                    
#                     if id  not in present_student_ids:
#                         name=id_name_map.get(id,"Unknown")
#                         subject_name=subject_id_name_map.get(subject_id,"Unknown Subject")
#                         records.append({
#                             "timestamp": timestamp,
#                             "student_id":id,
#                             "subject_id": subject_id,
                            
#                             "is_present": is_present
                            
#                         })
#                         show.append({
#                             "timestamp": timestamp,
                            
#                             "student_id": id,
#                             "name":name,
                            
                            
#                             "subject_name":subject_name,
                            
#                             "present": "Present ✅" if is_present else "Absent ❌"
#                         })
#                     present_student_ids.add(id)
#             confirm_attendance_dialog(records,show)    
              
              

#         else:
#             st.error("please add audio to take attendance")