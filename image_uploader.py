import streamlit as st

image = st.file_uploader('Upload an image')
st.image(image)
