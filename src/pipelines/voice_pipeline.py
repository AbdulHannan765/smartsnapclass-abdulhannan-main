# from resemblyzer import VoiceEncoder ,preprocess_wav
# import numpy as np
# import io

# import librosa 
# import streamlit as st
# @st.cache_resource
# def  load_voice_encoder():
#     return VoiceEncoder()
# def get_voice_embedding(voice_bytes):
#         try:
#             voice_encoder=load_voice_encoder()
#             audio,sr=librosa.load(io.BytesIO(voice_bytes),sr=16000)
#             wav=preprocess_wav(audio)
#             embedding=voice_encoder.embed_utterance(wav)
#             return embedding.tolist()
            
#         except Exception as e:
             
#              st.error(f"voice recognition error: {e}")
#              print(e)
#              import time
#              st.write("hmmm")
#              time.sleep(5)
#              return None
# def identify_voice(passed_voice,all_voice_dict,threshold=0.65):
#      if not passed_voice or not all_voice_dict:
#           return None,0.0
#      best_score=-1
#      best_id=None
#      for id,voice in all_voice_dict.item():
#           similarity_score=np.dot(passed_voice,all_voice_dict)
#           if similarity_score>best_score:
#                best_id=id
#                best_score=similarity_score
#      if best_score<=threshold:
#           return best_id,best_score
#      return None,best_score
# def process_bulk_voice(passed_voice,all_voice_dict):
#      try:
#           identified_results={}
#           voice_encoder=load_voice_encoder()
#           import tempfile

#           with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
#                     tmp.write(passed_voice)
#                     tmp_path = tmp.name

#           audio, sr = librosa.load(tmp_path, sr=16000)
#           segments = librosa.effects.split(audio, top_db=15)
#           for start,end in segments:
#                duration = (end - start) / sr 
#                if duration<0.5:
#                     continue
#                voice=audio[start:end]
#                voice_embedding=get_voice_embedding(voice)
#                id,score=identify_voice(voice_embedding)
#                print("Audio length:", len(audio))
#                print("Sample rate:", sr)
#                print("Segments:", segments)
#                if id not in identified_results or score>identified_results[id]:
#                     identified_results[id]=score
#           return identified_results
#      except Exception as e:
#           st.error(f"bulk voce recognition error: {e}")
                    



               
     