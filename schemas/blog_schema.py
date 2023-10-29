from pydantic import BaseModel
from typing import List

class BlogCreate(BaseModel):
    title: str
    content: str
    author: str
    tags: List[str] = []

class BlogRequest(BaseModel):
    id: str
    published_at: str
    title: str
    content: str
    author: str
    tags: List[str] = []

class BlogUpdate(BaseModel):
    title: str
    content: str
    author: str
    tags: List[str] = []

blogArticleDB: list[BlogCreate] = [{}]