# LangChain Ollama Chatbot

A simple Streamlit chatbot built with LangChain and Ollama.

## Features

- LangChain prompt template and output parser
- Local Ollama LLM using the llama2 model
- Streamlit web interface
- Optional LangSmith tracing configuration

## Project Structure

```text
.
├── chatbotwithlama.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama and make sure the `llama2` model is available locally.

## Run

```bash
streamlit run chatbotwithlama.py
```

## Configuration

Copy `.env.example` to `.env` and add your own LangSmith credentials if you want tracing.

Do not commit your `.env` file or credentials to the repository.
