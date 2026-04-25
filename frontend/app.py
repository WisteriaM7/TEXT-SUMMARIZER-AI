import streamlit as st
import requests

st.set_page_config(
    page_title="LLaMA Text Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("📝 LLaMA Text Summarizer")
st.markdown("Powered by **LLaMA via Ollama** · FastAPI backend · Streamlit frontend")
st.divider()

user_input = st.text_area(
    "Enter your text here:",
    placeholder="Paste any article, paragraph, or long text you'd like summarized...",
    height=250
)

col1, col2 = st.columns([1, 4])
with col1:
    summarize_btn = st.button("Summarize", type="primary", use_container_width=True)
with col2:
    if st.button("Clear", use_container_width=True):
        st.rerun()

if summarize_btn:
    if not user_input.strip():
        st.warning("⚠️ Please enter some text before summarizing.")
    else:
        with st.spinner("Generating summary..."):
            try:
                response = requests.post(
                    "http://localhost:8000/summarize/",
                    data={"text": user_input},
                    timeout=90
                )
                result = response.json()

                if "summary" in result:
                    st.subheader("🔍 Summary")
                    st.success(result["summary"])
                elif "error" in result:
                    st.error(f"❌ Error: {result['error']}")
            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to the backend. Make sure FastAPI is running on port 8000.")
            except Exception as e:
                st.error(f"❌ Unexpected error: {str(e)}")

st.divider()
st.caption("Make sure Ollama is running (`ollama serve`) and the FastAPI backend is active (`uvicorn backend.main:app --reload`) before using the app.")
