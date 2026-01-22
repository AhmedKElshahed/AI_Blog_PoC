from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class BlogRequest(BaseModel):
    prompt: str = Field(..., min_length=3)
    target_audience: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    tone: Optional[str] = None
    language: Optional[str] = "en"
    blog_length: Optional[Literal["short", "medium", "long"]] = "medium"
    niche: Optional[str] = None
    keywords: Optional[List[str]] = None
