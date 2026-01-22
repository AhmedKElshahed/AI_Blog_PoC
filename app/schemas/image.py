from pydantic import BaseModel, Field
from typing import List, Dict

class ImagePrompts(BaseModel):
    visual_style: str
    hero_image_prompt: str
    section_image_prompts: List[str] = Field(default_factory=list)
    negative_prompt: str
    aspect_ratios: Dict[str, str] = Field(default_factory=lambda: {"hero": "16:9", "section": "4:3"})
