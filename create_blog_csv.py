import csv

header = ["id", "published_at", "title", "content", "author", "publish_at", "tags"]

with open("blog_database.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(header)