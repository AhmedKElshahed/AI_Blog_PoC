from app.schemas.input import BlogRequest
from app.agents import seo_refiner, blog_writer, image_prompt_builder

async def generate(req: BlogRequest) -> dict:
    seo = await seo_refiner.run(req)
    blog = await blog_writer.run(req, seo)
    images = await image_prompt_builder.run(req, seo, blog)

    return {
        "seo_plan": seo.model_dump(),
        "blog": blog.model_dump(),
        "image_prompts": images.model_dump(),
    }
