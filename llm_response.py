import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TOGETHER_API_KEY")
BASE_URL = "https://api.together.xyz/v1/chat/completions"
MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"

def get_llm_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a career guidance AI assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 800,
        "temperature": 0.7,
        "top_p": 0.9,
        "repetition_penalty": 1.2
    }

    try:
        res = requests.post(BASE_URL, headers=headers, json=data)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
