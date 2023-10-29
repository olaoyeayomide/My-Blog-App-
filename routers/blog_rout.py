import csv
from fastapi import APIRouter, Path, HTTPException, Depends
from schemas.blog_schema import BlogCreate, BlogRequest, BlogUpdate
from services.blog_service import BlogService
# from uuid import UUID
from typing import List

blog_service = BlogService()
blog_router = APIRouter()

blogDB: List[BlogRequest] = []


def get_blog():
    return blogDB


# Create Blog
@blog_router.post("/blog/")
async def create_blog(blog_data: BlogCreate):
    response = blog_service.create_blog_service(blog_data, blogDB)
    blogDB.append(response)
    return {"message": "Blog Created Successfully", "data": response}


# Get Blog Post
@blog_router.get("/blog/{id}")
async def get_blog_post(id: str = Path(..., title="The ID of the blog")):
    blog = blog_service.get_blog_post_service(blogDB, id)

    if not blog:
        raise HTTPException(status_code=404, detail="Sorry We Are Unable To Find This Blog. Please Try Again")
    else:
        response = {"message": f"Blog With {id} Has Been Found", "data": blog}
        return response
    

# Edit Blog Post
@blog_router.put("/edit_blog", response_model=BlogRequest)
async def edit_blog_post(id: str, update_data: BlogUpdate):
    updated_blog = blog_service.edit_blog_post_service(id, update_data, blogDB)
    if not updated_blog:
        raise HTTPException(status_code=404, detail="Sorry We Are Unable To Edit This Blog Because It Can't Be Found. Please Try Again")
    return updated_blog


# Get Blogs
@blog_router.get("/blogs")
async def get_blogs():
    return blogDB

# Delete User
@blog_router.delete("/delete_user/{blog_id}")
def delete_blog(id: str):
    result = blog_service.delete_blog_service(id)

    if result is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": f"User With ID {id} Has Been Deleted Successfully"}
