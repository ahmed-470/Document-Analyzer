import streamlit as st
from src.ui.interface import run_interface

if __name__ == '__main__':
    st.set_page_config(page_title="RAG Doc Analyzer", layout="wide")
    run_interface()