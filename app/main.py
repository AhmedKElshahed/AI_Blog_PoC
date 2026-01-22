from fastapi import FastAPI
from app.schemas.input import BlogRequest
from app.pipeline import generate

app = FastAPI(title="AI Blog Generator PoC")

@app.post("/generate_blog")
async def generate_blog(req: BlogRequest):
    return await generate(req)
