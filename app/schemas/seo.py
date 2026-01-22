from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class OutlineSection(BaseModel):
    h2: str
    h3: List[str] = Field(default_factory=list)

class SEOPlan(BaseModel):
    primary_keyword: str
    secondary_keywords: List[str] = Field(default_factory=list)
    search_intent: Literal["informational", "commercial", "transactional", "navigational"] = "informational"
    title_options: List[str] = Field(min_length=3)
    slug_suggestion: str
    outline: List[OutlineSection]
    internal_link_suggestions: List[str] = Field(default_factory=list)
    meta_title_draft: str
    meta_description_draft: str
    content_prompt: str
