# LangChain Groq + Ollama API

A simple Generative AI project that combines **FastAPI**, **LangServe**, **LangChain**, **Groq**, **Ollama**, and **Streamlit**.

The application exposes LangChain chains through API endpoints and provides a Streamlit client for generating essays with Groq's `openai/gpt-oss-20b` model and poems with a local Ollama `llama2` model.

## Features

- FastAPI backend
- LangServe API routes
- Groq integration with `openai/gpt-oss-20b`
- Local Ollama integration with `llama2`
- Streamlit frontend
- LangChain prompt templates
- Environment-variable based API key configuration

## Project Structure

```text
.
├── app.py
├── client.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Groq

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file or API key to GitHub.

### 3. Set up Ollama

Install Ollama and make sure the `llama2` model is available locally:

```bash
ollama pull llama2
```

## Run the API

Start FastAPI from the project directory:

```bash
python app.py
```

The API runs at:

```text
http://localhost:8000
```

Available LangServe endpoints:

- `/groq`
- `/essay`
- `/poem`

## Run the Streamlit Client

Open a second terminal and run:

```bash
streamlit run client.py
```

Then open the local Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Architecture

```text
Streamlit Client
       |
       v
FastAPI + LangServe
   |           |
   v           v
 Groq       Ollama
GPT-OSS     Llama 2
```

## Notes

- Groq requires a valid `GROQ_API_KEY`.
- Ollama runs locally and does not require an API key.
- The Streamlit client expects the FastAPI server to be running on `localhost:8000`.
