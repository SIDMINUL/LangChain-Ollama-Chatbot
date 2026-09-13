import requests
import streamlit as st


def get_groq_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {"topic": input_text}}
    )
    response.raise_for_status()
    return response.json()["output"]["content"]


def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input": {"topic": input_text}}
    )
    response.raise_for_status()
    return response.json()["output"]["content"]


st.title("LangChain Demo with Groq and Ollama")

input_text = st.text_input("Enter a topic for essay")
input_text1 = st.text_input("Enter a topic for poem")

if input_text:
    essay_response = get_groq_response(input_text)
    st.write("Essay Response:")
    st.write(essay_response)

if input_text1:
    poem_response = get_ollama_response(input_text1)
    st.write("Poem Response:")
    st.write(poem_response)
