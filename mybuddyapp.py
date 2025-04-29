import streamlit as st
import os
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

st.title("🤖 My Buddy")

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

models = ["llama3.2", "gpt-4o-mini"]
selection = st.sidebar.selectbox("Models", models)


def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "how is the weather today?",
    )
    submitted = st.form_submit_button("Submit")
    generate_response(text)
