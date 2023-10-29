from fastapi import FastAPI
from routers.user_rout import user_router
from routers.blog_rout import blog_router

app = FastAPI()

app.include_router(user_router)
app.include_router(blog_router)

@app.get("/")
def home():
    return {"message": "Welcome To My Blog. Sign Up to discover why millions of people have realize their dreams here"}

# About Blog
@app.get("/about")
def about():
    return {"message": "Share breaking news or whatever's on your mind, we got you covered at MY BLOG. Sign Up to discover why millions of people have realize their dreams here"}

# Contact Details
@app.get("/contact")
async def contact():
    return {"message": "For More Enquirer Contact Us At Our Email: explore@blog.org or kindly call 08165172990"
    }