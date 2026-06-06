import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with st.sidebar:
    st.title("Settings")
    st.write("Powered by Gemini AI")

st.title("AI Chatbot")

question = st.chat_input("Type your message...")

if question:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    with st.chat_message("assistant"):
        st.write(response.text)