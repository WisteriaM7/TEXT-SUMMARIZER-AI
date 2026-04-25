from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI(title="LLaMA Text Summarizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "LLaMA Text Summarizer API is running!"}

@app.post("/summarize/")
def summarize(text: str = Form(...)):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama2",
                "prompt": f"Summarize the following text clearly and concisely:\n\n{text}",
                "stream": False
            },
            timeout=60
        )
        result = response.json()
        return {"summary": result["response"]}
    except requests.exceptions.ConnectionError:
        return {"error": "Could not connect to Ollama. Make sure Ollama is running on port 11434."}
    except Exception as e:
        return {"error": str(e)}
