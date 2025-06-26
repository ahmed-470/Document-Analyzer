import streamlit as st
from src.graph.executor import run_rag_pipeline
from src.state.session_manager import get_session_state


def run_interface():
    st.title("📄 RAG Document Analyzer")

    session = get_session_state()

    # API Key Input
    if not session.get("api_key"):
        session.api_key = st.text_input("Enter OpenAI API Key", type="password")
        if not session.api_key:
            st.warning("Please enter your OpenAI API key to continue.")
            return

    # Upload or Paste Document
    doc_input = st.text_area("Paste your document here", height=200)
    uploaded_file = st.file_uploader("Or upload a UTF-8 text file", type="txt")

    if uploaded_file:
        doc_input = uploaded_file.read().decode("utf-8")

    if doc_input:
        session.document = doc_input

    # Natural Language Query
    '''
    query = st.text_input("Ask a question about the document")
    if st.button("Run Query") and query:
        with st.spinner("Processing..."):
            response = run_rag_pipeline(query, session.document, session.api_key)
            st.markdown("### Response")
            st.write(response)
    '''
    query = st.text_input("Ask a question about the document")
    if st.button("Run Query") and query:
        with st.spinner("Processing..."):
            response = run_rag_pipeline(query, session.document, session.api_key)

            # ✅ Save to chat history
            session.history.append((query, response))

            st.markdown("### Response")
            st.write(response)

    # Chat History
    st.markdown("---")
    st.markdown("### Chat History")
    for q, a in session.history:
        st.markdown(f"**Q:** {q}")
        st.markdown(f"**A:** {a}")
