import csv
from schemas.blog_schema import BlogCreate, BlogRequest, BlogUpdate
from uuid import UUID
from fastapi import HTTPException
from typing import List
from datetime import datetime
from typing import List

# Dummy DataBase
blogDB: List[BlogRequest] = []

# def get_blog():
#     return blogDB


class BlogService:

    # Create Blog
    def create_blog_service(self, blog_data: BlogCreate, blogDB: List[BlogRequest]):
        with open("blog_database.csv", "a", newline='') as file:
            writer = csv.writer(file)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            blog_id = str(UUID(int=len(blogDB) + 1))
            writer.writerow([blog_id, current_time, blog_data.title, blog_data.content, blog_data.author,",".join(blog_data.tags)])

        blog = BlogRequest(id=blog_id, published_at=current_time, **blog_data.dict())
        blogDB.append(blog)

        return blog

    
# Get Blog POst
    def get_blog_post_service(self, blogDB: List[BlogRequest], id: str):
        for blog in blogDB:
            if blog.id == id:
                return blog

                # with open('blog_database.csv', "a", newline='') as file:
                #     writer = csv.writer(file)
                #     writer.writerow([blog.id, blog.title, blog.content,blog.author, blog.published_at, blog.tags])
                # return blog
            

# Edit Blog Post
    def edit_blog_post_service(self, id: str, update_data: BlogUpdate, blogDB: List[BlogRequest]):
        for blog in blogDB:
            if blog.id == id:
                title = str(update_data.title)
                content = str(update_data.content)
                author = str(update_data.author)
                tags = str(update_data.tags)

                current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                blog.title = title
                blog.content = content
                blog.author = author
                blog.published_at = current_datetime
                blog.tags = tags


                rows = []
                with open("blog_database.csv", 'r') as f:
                    reader = csv.reader(f)
                    header = next(reader)
                    for row in reader:
                        if len(row) > 0 and row[0] == id:
                            row = [id, title, content, author, current_datetime, ",".join(tags)]
                        rows.append(row)

                with open('blog_database.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(rows)

                updated_blog = blog
                break

        return updated_blog
            

# Delete Blog
    def delete_blog_service(self, id: str, column_index: int = 0):
        rows = []
        with open("blog_database.csv", 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if row and len(row) > column_index and row[column_index] == id:
                    continue
                rows.append(row)

        with open('blog_database.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for row in rows:
                    writer.writerow(row)

        return {"message": "Blog Deleted"}
