# Q&A Chatbot
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st

## Function to load OpenAI model and get respones
def get_openai_response(question):
    llm = OpenAI(model_name="text-davinci-003",temperature=0.5)
    response=llm(question)
    return response


st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")
if submit:
    st.subheader("The Response is")
    st.write(response)