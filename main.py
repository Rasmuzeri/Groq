from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()

GROQ_API_KEY = "API_KEY_HERE"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

MODEL_NAME = "llama3-8b-8192"

class TranslationRequest(BaseModel):
    text: str

class SentimentRequest(BaseModel):
    text: str

@app.post("/translate")
def translate_text(request: TranslationRequest):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a translator that translates English to Finnish."},
            {"role": "user", "content": request.text}
        ]
    }
    
    response = requests.post(GROQ_API_URL, json=payload, headers=headers)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    result = response.json()
    translated_text = result["choices"][0]["message"]["content"]
    return {"translated_text": translated_text}

@app.post("/sentiment")
def analyze_sentiment(request: SentimentRequest):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a sentiment analyzer that determines if the sentiment is positive, neutral, or negative."},
            {"role": "user", "content": request.text}
        ]
    }
    
    response = requests.post(GROQ_API_URL, json=payload, headers=headers)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    result = response.json()
    sentiment = result["choices"][0]["message"]["content"]
    return {"sentiment": sentiment}
