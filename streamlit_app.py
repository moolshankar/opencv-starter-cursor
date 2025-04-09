import streamlit as st
import requests
import os
from PIL import Image
import io

st.title("Face Detection System")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Upload Images", "Train Model", "Face Detection"])

if page == "Upload Images":
    st.header("Upload Images for Training")
    
    name = st.text_input("Enter person's name")
    uploaded_files = st.file_uploader("Choose images (minimum 4)", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])
    
    if st.button("Upload"):
        if not name:
            st.error("Please enter a name")
        elif len(uploaded_files) < 4:
            st.error("Please upload at least 4 images")
        else:
            files = [("images", file) for file in uploaded_files]
            try:
                response = requests.post(
                    "http://localhost:8000/api/images/upload",
                    params={"name": name},
                    files=files
                )
                if response.status_code == 200:
                    st.success("Images uploaded successfully!")
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Error connecting to server: {str(e)}")

elif page == "Train Model":
    st.header("Train Face Recognition Model")
    
    if st.button("Train Model"):
        try:
            response = requests.post("http://localhost:8000/api/model/train")
            if response.status_code == 200:
                st.success("Model trained successfully!")
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Error connecting to server: {str(e)}")

elif page == "Face Detection":
    st.header("Real-time Face Detection")
    
    if st.button("Start Detection"):
        try:
            response = requests.post("http://localhost:8000/api/video/start")
            if response.status_code == 200:
                st.success("Face detection started!")
                st.info("Press 'q' in the OpenCV window to stop detection")
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Error connecting to server: {str(e)}")

# Add some styling
st.markdown("""
<style>
.stButton>button {
    width: 100%;
    height: 3em;
}
</style>
""", unsafe_allow_html=True) 