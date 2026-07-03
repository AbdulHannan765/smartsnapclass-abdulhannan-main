import streamlit as st
import base64
from src.ui.base_layout import hide_streamlit_layout,home_font_and_style
def des():
    st.set_page_config(
            page_title="Smart AI Attendance | Landing Page",
            page_icon="📸",
            layout="wide",
            initial_sidebar_state="collapsed"
        )
    st.markdown("""
        <style>
    
    
    
    
    
    
        /* Paragraphs, markdown, lists */
        p, li, span {
            color: white !important;
        }
    
        /* Streamlit Markdown */
    
        /* Tabs */
        button[data-baseweb="tab"] {
            color: white !important;
        }
    
        /* Widget labels */
        label {
            color: white !important;
        }
    
        /* Info, success, warning text */
        [data-testid="stAlert"] * {
            color: white !important;
        }
    
        /* Expanders */
        .streamlit-expanderHeader {
            color: white !important;
        }
    
    
        </style>
        """, unsafe_allow_html=True)
def landing_page():
    des()
    home_font_and_style()
    hide_streamlit_layout()
    
    if st.button("GO TO MAIN APP"):
       
        st.session_state["login_type"]="home_screen"
        st.rerun()
    with open("pics/background.png", "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)

    # --- PAGE CONFIGURATION ---
  

    # --- CUSTOM CSS & HTML ---
    st.markdown("""
        <style>
        /* Global styles */
        .hero-container {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, #2b5876 0%, #4e4376 100%);
            border-radius: 15px;
            color: white;
            margin-bottom: 2rem;
        }
        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            font-family: 'Arial Black', sans-serif;
        }
        .hero-subtitle {
            font-size: 1.2rem;
            font-weight: 300;
            opacity: 0.9;
        }
        .feature-card {
            background-color: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #ff4b4b;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .section-header {
            color: white;
            border-bottom: 2px solid #ff4b4b;
            padding-bottom: 10px;
            margin-top: 2rem;
            margin-bottom: 1.5rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">Smart AI Attendance</div>
            <div class="hero-subtitle">Next-Generation Facial Recognition System for Modern Classrooms</div>
        </div>
    """, unsafe_allow_html=True)


    # --- CORE FLOW SECTION ---
    st.markdown("<h2 class='section-header'>⚙️ Core Workflow & Architecture</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("""
        ### How it works
        Our system utilizes an advanced **Support Vector Classifier (SVC)** model to generate and classify facial embeddings, ensuring seamless and spoof-proof attendance.
        """)
        st.image("pics/face_ana.png", caption="Real-time AI Face Scanning", width="stretch")

    with col2:
        st.markdown("""
        <div class="feature-card"><b>Step 1: Student Registration</b><br>Students register by capturing their face. The system verifies and captures the primary photo.</div>
        <div class="feature-card"><b>Step 2: Embedding Generation</b><br>AI model creates unique photo embeddings and securely stores the student’s biometric info in the database.</div>
        <div class="feature-card"><b>Step 3: Subject Enrollment</b><br>Students enroll in specific subjects using unique subject codes created by their respective faculty.</div>
        <div class="feature-card"><b>Step 4: Flexible Capture</b><br>Faculty can click or upload a single group photo of the whole class, or multiple photos containing varying numbers of students.</div>
        <div class="feature-card"><b>Step 5: Automated Analysis</b><br>Faculty triggers 'Run Face Analysis'. The SVC model identifies student IDs in the photos, marks them present, and updates the database instantly.</div>
        """, unsafe_allow_html=True)


    st.divider()

    # --- FEATURES SHOWCASE (TABS) ---
    st.markdown("<h2 class='section-header'>📱 Platform Features</h2>", unsafe_allow_html=True)

    tab_faculty, tab_student = st.tabs(["👨‍🏫 Faculty Portal", "🎓 Student Portal"])

    # --- FACULTY PORTAL ---
    with tab_faculty:
        st.markdown("### Empowering Educators with Effortless Tracking")
        
        fac_col1, fac_col2 = st.columns(2)
        
        with fac_col1:
            st.markdown("**1. Secure Faculty Login**")
            st.image("pics/faculty_login.png", caption="Faculty Authentication Screen",  width="stretch")
            
            st.markdown("**3. Seamless Subject Management**")
            st.image("pics/faculty_dashbord.png", caption="Faculty Dashboard (Manage Subjects & Track Records)",  width="stretch")
            
            st.markdown("**5. Versatile Photo Upload**")
            st.image("pics/photo_uplaod.png", caption="Upload Multiple Pre-captured Class Photos", width="stretch")

        with fac_col2:
            st.markdown("**2. Create Custom Subjects**")
            st.image("pics/subjects.png", caption="Define Subject Name, Code, and Section",  width="stretch")
            
            st.markdown("**4. Direct Attendance Interface**")
            st.image("pics/face_analysis.png", caption="Select Subject & Trigger Face Analysis",  width="stretch")
            
            st.markdown("**6. Live Camera Integration**")
            # st.image("Screenshot 2026-07-03 160500.png", caption="Click Photos directly from the Web Interface", use_column_width=True)

    # --- STUDENT PORTAL ---
    with tab_student:
        st.markdown("### Frictionless Onboarding for Students")
        
        stu_col1, stu_col2 = st.columns(2)
        
        with stu_col1:
            st.markdown("**1. One-Time Profile Creation**")
            st.image("pics/registor.png", caption="Student Registration Screen",  width="stretch")
            
            st.markdown("**3. Clean Dashboard**")
            st.image("pics/enroled.png", caption="View Enrolled Subjects and Attendance Stats",  width="stretch")

        with stu_col2:
            st.markdown("**2. Subject Enrollment**")
            st.image("pics/enroling.png", caption="Enroll via Faculty-provided Subject Code", width="stretch")
            
            st.markdown("**4. Automated Feedback**")
            st.info("Once a student's face is registered, they simply walk into class. The AI handles the rest when the faculty takes the class picture, saving 10-15 minutes of traditional roll-call time!")

    # --- FOOTER ---
    st.divider()
    st.markdown("""
        <div style='text-align: center; color: #666;'>
            <p>Built with Streamlit • Python • Support Vector Classifiers</p>
        </div>
    """, unsafe_allow_html=True)