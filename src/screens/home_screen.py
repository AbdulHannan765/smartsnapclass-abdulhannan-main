import streamlit as st
from src.components.header import header
from src.ui.base_layout import style_backround_home
from src.ui.base_layout import   style_login_backround
from src.ui.base_layout import   hide_streamlit_layout
from src.ui.base_layout import  home_font_and_style

def home_screen():
   
    
   
    header()
    style_backround_home()
    hide_streamlit_layout()
    home_font_and_style()

   
    st.markdown("""
        <div style="text-align: center; margin-top: -20px;">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135755.png" width="180">
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, spacer, col2 = st.columns([1, 0.2, 1])

    with col1:
        if st.button("🎓 Teacher Portal", type="primary", use_container_width=True):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    with col2:
        if st.button("👨‍🎓 Student Portal", type="secondary", use_container_width=True):
            st.session_state["login_type"] = "student"
            st.rerun()
    
    for _ in range(12):
     st.write("")
    col1,col2,col3,col4=st.columns(4)
    with col4:
       st.markdown(
        "<h3 style='white-space:nowrap;'>Created By Abdul Hannan ❤️</h3>",
        unsafe_allow_html=True
     )