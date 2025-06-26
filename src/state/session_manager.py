import streamlit as st

def get_session_state():
    if "document" not in st.session_state:
        st.session_state.document = ""
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    if "history" not in st.session_state:
        st.session_state.history = []
    return st.session_state