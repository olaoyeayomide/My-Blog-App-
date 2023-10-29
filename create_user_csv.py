import csv

header = ["id", "created_at","first_name", "last_name", "user_name", "bio", "email", "password"]

with open("user_database.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(header)