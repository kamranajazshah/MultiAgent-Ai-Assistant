import streamlit as st
import requests
from agent import run_agent
st.set_page_config(page_title="🧠 LangChain Multi-Tool AI Assistant")
st.title("🧠 LangChain Multi-Tool AI Assistant")
url= "http://localhost:8000/ask"
user_input = st.text_input("Ask your question here:")
if user_input:
    with st.spinner("Thinking"):
        try:
            response=requests.post(url=url,json={"question":user_input})
            if response.status_code == 200:
                answer = response.json()["answer"]
                st.markdown("**Answer:**")
                st.write(answer)
            else:
                st.error(f" Server error: {response.text}")
        except Exception as e:
            st.error(f" Error: {e}") 
