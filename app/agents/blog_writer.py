from app.llm.ollama_client import generate_json
from app.schemas.blog import BlogDraft
from app.schemas.seo import SEOPlan
from app.schemas.input import BlogRequest

SYSTEM = """You are a senior blog writer skilled in SEO formatting.
Return ONLY valid JSON. No markdown. No extra keys.
Write clean HTML. Use <h1>, <h2>, <h3>, <p>, <ul><li>.
No fake citations or made-up data. If uncertain, speak generally."""

async def run(req: BlogRequest, seo: SEOPlan) -> BlogDraft:
    user = {
        "final_content_prompt": seo.content_prompt,
        "seo_plan": seo.model_dump(),
        "constraints": {
            "language": req.language,
            "tone": req.tone,
            "length": req.blog_length,
        },
        "output_format": "BlogDraft JSON",
    }
    return await generate_json(SYSTEM, str(user), BlogDraft)
