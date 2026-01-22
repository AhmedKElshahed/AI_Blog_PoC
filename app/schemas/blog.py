from pydantic import BaseModel, Field
from typing import List, Dict

class FAQItem(BaseModel):
    q: str
    a: str

class BlogDraft(BaseModel):
    slug: str
    meta_title: str
    meta_description: str
    article_html: str
    summary: str
    faq: List[FAQItem] = Field(default_factory=list)
    image_alt_texts: List[str] = Field(default_factory=list)
