import streamlit as st
import segno
import io
@st.dialog("Share Class Link")
def share_subject(subject_name,subject_code):
    app_domain="smartsnapclass-main.streamlit.app"
    url = f"{app_domain}?join_code={subject_code}"
    st.header("SCAN")
    qr=segno.make(url)
    out=io.BytesIO()
    qr.save(out,kind="png",scale=10,border=1)
    col1,col2=st.columns(2)
    with col1:
        st.markdown("### COPY LINK")
        st.code(url,language="text")
        st.code(subject_code,language="text")
        st.info("copy this link to share")
    with col2:
        st.markdown(" scan to join")
        st.image(out.getvalue(),width=200,caption="QRcode for class joining ")


