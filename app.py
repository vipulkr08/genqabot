from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")


def get_gemini_response(question):
    response = model.generate_content(question)
    try:
        return response.text
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


st.set_page_config(page_title="GenqaBot", page_icon="logo.png", layout="wide")
st.title("GenqaBot")


st.write(
    """
    Welcome to Genqa Chatbot! Ask any question, and Genqa will provide you with an insightful response.
    This chatbot is powered by Generative AI. Feel free to explore and discover the knowledge Genqa has to offer.
    """
)

st.write(
    "Get started by entering a question in the input box below and clicking on 'Ask the question.'"
)

st.sidebar.header("Instructions")
st.sidebar.markdown(
    "Type your question in the input box and click 'Ask the question' to get a response."
)

input_question = st.text_input("Ask a question:", key="input")
submit_button = st.button("Ask the question")

if submit_button:
    if input_question:
        response = get_gemini_response(input_question)
        st.subheader("Response: ")
        if response:
            st.info(response)
        else:
            st.warning(
                "Sorry, Genqa couldn't answer that question. Please try another one."
            )
    else:
        st.warning("Please enter a question before asking.")

st.markdown(
    """
    <style>
        div[data-baseweb="toast"] {
            background-color: #82c7f4;
            color: #1a1a1a;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
