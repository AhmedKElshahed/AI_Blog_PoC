from app.llm.ollama_client import generate_json
from app.schemas.seo import SEOPlan
from app.schemas.input import BlogRequest

SYSTEM = """You are an SEO strategist and prompt engineer.
Return ONLY valid JSON. No markdown. No extra keys.
Make a practical SEO plan and a final content_prompt for a blog writer agent.
Avoid fake statistics. If you include numbers, make them generic or clearly framed as examples."""

async def run(req: BlogRequest) -> SEOPlan:
    user = {
        "user_prompt": req.prompt,
        "target_audience": req.target_audience,
        "country": req.country,
        "city": req.city,
        "tone": req.tone,
        "language": req.language,
        "blog_length": req.blog_length,
        "niche": req.niche,
        "keywords": req.keywords,
        "instructions": [
            "If keywords are provided, use them. If not, suggest them.",
            "Output slug_suggestion in the same language, lowercase with hyphens.",
            "Outline must contain 5-8 H2 sections with optional H3s.",
            "Include FAQ section in outline.",
            "content_prompt must instruct blog writer to produce HTML with headings and short paragraphs.",
        ],
        "output_format": "SEOPlan JSON",
    }
    return await generate_json(SYSTEM, str(user), SEOPlan)
