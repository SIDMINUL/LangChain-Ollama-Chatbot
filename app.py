from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using Groq and Ollama"
)

add_routes(
    app,
    ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0
    ),
    path="/groq"
)

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

llm = ChatOllama(
    model="llama2",
    temperature=0
)

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)
prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} with 100 words"
)

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
