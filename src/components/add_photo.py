import streamlit as st

from PIL import Image

import streamlit as st
from PIL import Image

@st.dialog("add photos")
def add_photos_dialogue():

    # Initialize session state
    if "attendance_images" not in st.session_state:
        st.session_state["attendance_images"] = []

    if "camera_added" not in st.session_state:
        st.session_state["camera_added"] = False

    if "upload_added" not in st.session_state:
        st.session_state["upload_added"] = False

    if "add_photo" not in st.session_state:
        st.session_state["add_photo"] = "camera"

    st.header("Add Photos")

    # Correct column usage
    col1, col2 = st.columns(2)

    with col1:
        type_of_photo = "primary" if st.session_state["add_photo"] == "camera" else "secondary"
        if st.button("Click photo", type=type_of_photo):
            st.session_state["add_photo"] = "camera"
            st.session_state["camera_added"] = False   # reset
            st.rerun()

    with col2:
        type_of_photo = "primary" if st.session_state["add_photo"] == "upload" else "secondary"
        if st.button("Upload photos", type=type_of_photo):
            st.session_state["add_photo"] = "upload"
            st.session_state["upload_added"] = False   # reset
            st.rerun()

    if st.session_state["add_photo"] == "camera":
        image = st.camera_input("Click your photo")

        if image and not st.session_state["camera_added"]:
            image = Image.open(image)
            st.session_state["attendance_images"].append(image)
            st.session_state["camera_added"] = True
            st.toast("Photo added successfully")

   
    if st.session_state["add_photo"] == "upload":
        images = st.file_uploader(
            "Upload photos",
            accept_multiple_files=True,
            type=["jpg", "jpeg", "png"]
        )

        if images and not st.session_state["upload_added"]:
            for img in images:
                image = Image.open(img)
                st.session_state["attendance_images"].append(image)

            st.session_state["upload_added"] = True
            st.toast(f"{len(images)} photos uploaded successfully")

    if st.button("Done"):
        st.session_state["camera_added"] = False
        st.session_state["upload_added"] = False
        st.rerun()