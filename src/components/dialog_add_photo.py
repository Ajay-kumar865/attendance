import streamlit as st
from PIL import Image

@st.dialog("Add Photos")
def add_photos_dialog():
    st.write("Upload classroom photos to take attendance.")
    
    uploaded_files = st.file_uploader(
        "Upload Classroom Photos",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )
    
    camera_photo = st.camera_input("Or take a photo now")
    
    if st.button("Add to Analysis", type="primary", width="stretch"):
        added_count = 0
        if "attendance_images" not in st.session_state:
            st.session_state.attendance_images = []
            
        if uploaded_files:
            for f in uploaded_files:
                img = Image.open(f).convert("RGB")
                st.session_state.attendance_images.append(img)
                added_count += 1
                
        if camera_photo:
            img = Image.open(camera_photo).convert("RGB")
            st.session_state.attendance_images.append(img)
            added_count += 1
            
        if added_count > 0:
            st.toast(f"Added {added_count} photo(s) successfully!")
            st.rerun()
        else:
            st.warning("Please upload or capture at least one photo.")
