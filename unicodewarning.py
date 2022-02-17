import streamlit as st

if st.checkbox('UnicodeWarning'):
    raise UnicodeWarning('Manually raised UnicodeWarning')
