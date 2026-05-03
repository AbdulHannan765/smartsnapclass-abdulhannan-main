import streamlit as st
def style_backround_home():
    st.markdown("""
        <style>
        .stApp {
            background: #1DA7BF !important;
        }
        </style>
        """, unsafe_allow_html=True)
def style_login_backround():
    st.markdown("""
                <style>
                .stApp {
                    background: #D8F7F2 !important;
                }
                </style>

                """,unsafe_allow_html=True)
def hide_streamlit_layout():
    st.markdown("""
        <style>
            #MainMenu, footer, header {
                visibility : hidden;
            }
            

            .block-container {
              padding-top : 0.9rem !important;
                
            }
            
        </style>
    """, unsafe_allow_html=True)
def home_font_and_style():
    st.markdown("""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Sekuya&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&family=Sekuya&display=swap');

                h2{
                 font-family: 'Climate Crisis', sans-sarif !important;
                 font-size : 3.5rem !important;
                 line-height: 1.1 !important;
                 margin-bottom : 0rem !important;
                } 

                div[data-baseweb="input"] input {
                    font-size: 20px !important;
                    font-family: 'Climate Crisis', sans-serif !important;
                    }
                button[kind="primary"]{
                 background: #e7a436 !important;
                 color: white !important;
                 
                }
                button[kind="secondary"]{
                 background: #ff69b4 !important;
                 color : white !important;
                 
             
                }
                button[kind="tertiary"]{
                 background: #ff3d6e !important;
                 color : white !important;
                 padding: 4px ;
                 width:150px;
                 font-size:7px !important;
                 margin-bottom: 2px;
                 
             
                }
                button : hover{
                 transform : scale(1.05);}
                button[kind=["primary","secondary",tertiary"]] {
                    transition: transform 0.2s ease;
                    }
            </style>
    """,unsafe_allow_html=True)
def login_background_teacher():
    st.markdown("""
                  <style>
                    .stApp {
                        background: #896deb !important;
                    }
                  </style>
         
                """,unsafe_allow_html=True)
def login_background_student():
    st.markdown("""
        <style>
            .stApp{
                   background :#54cbf5 !important;
            }
        </style>
    """,unsafe_allow_html=True)
