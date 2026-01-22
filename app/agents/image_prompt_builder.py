from app.llm.ollama_client import generate_json
from app.schemas.images import ImagePrompts
from app.schemas.blog import BlogDraft
from app.schemas.seo import SEOPlan
from app.schemas.input import BlogRequest

SYSTEM = """You create image generation prompts for blog posts.
Return ONLY valid JSON. No markdown. No extra keys.
Prompts should be descriptive, camera/style-aware, and avoid text in the image."""

async def run(req: BlogRequest, seo: SEOPlan, blog: BlogDraft) -> ImagePrompts:
    user = {
        "blog_summary": blog.summary,
        "titles": seo.title_options,
        "niche": req.niche,
        "location": {"country": req.country, "city": req.city},
        "tone": req.tone,
        "style_rules": [
            "No text, no watermarks, no logos.",
            "Consistent style across all images.",
            "Prefer realistic photography unless niche implies illustration.",
        ],
        "output_format": "ImagePrompts JSON",
    }
    return await generate_json(SYSTEM, str(user), ImagePrompts)
