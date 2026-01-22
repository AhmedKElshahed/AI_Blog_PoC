import os, json
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
from pydantic import BaseModel

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b-instruct")

def _extract_json(text: str) -> str:
    # naive but effective: grab first {...} block
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object found in model output.")
    return text[start:end+1]

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.7, min=0.7, max=4))
async def generate_json(system: str, user: str, schema: type[BaseModel]) -> BaseModel:
    payload = {
        "model": OLLAMA_MODEL,
        "stream": False,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "options": {
            "temperature": 0.4,
        },
    }

    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(f"{OLLAMA_URL}/api/chat", json=payload)
        r.raise_for_status()
        data = r.json()

    text = data["message"]["content"]
    json_str = _extract_json(text)
    obj = json.loads(json_str)
    return schema.model_validate(obj)
