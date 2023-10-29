import csv
from fastapi import HTTPException
from schemas.user_schema import UserRequest, UserCreate, UserUpdate
from uuid import UUID
from pydantic import EmailStr
from datetime import datetime
from typing import List

userDB: List[UserRequest] = []


class UserService:

# Create User
    def create_user_service(self, user_data: UserCreate, userDB: List[UserRequest]):
        with open("user_database.csv", "a", newline='') as file:
            writer = csv.writer(file)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user_id = str(UUID(int=len(userDB) + 1))
            writer.writerow([user_id, current_time, user_data.first_name, user_data.last_name, user_data.username, user_data.bio, user_data.email, user_data.password])
        
        user= UserRequest(id=user_id, created_at=current_time, **user_data.dict())
        userDB.append(user)

        return user
    
#  Get User
    def get_user_service(self, userDB: List[UserRequest], id: str):
            for user in userDB:
                if user.id == id:
                    return user

                    # with open('user_database.csv', "a", newline='') as file:
                    #     writer = csv.writer(file)
                    #     writer.writerow([user.id, user.first_name, user.last_name,user.username, user.bio, user.email, user.password])
                    # return user
                

# Edit User
    def edit_user_service(self, id: str, update_data: UserUpdate, userDB: List[UserRequest]):
        updated_user = None
        for user in userDB:
            if user.id == id:
                first_name = str(update_data.first_name)
                last_name = str(update_data.last_name)
                username = str(update_data.username)
                bio = str(update_data.bio)
                email = str(update_data.email)
                password = str(update_data.password)

                current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.bio = bio
                user.email = email
                user.created_at = current_datetime
                user.password = password

                rows = []
                with open("user_database.csv", 'r') as f:
                    reader = csv.reader(f)
                    header = next(reader)
                    for row in reader:
                        if len(row) > 0 and row[0] == id:
                            row = [id, first_name, last_name, username, current_datetime, bio, email, password]
                        rows.append(row)

                with open('user_database.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(rows)

                updated_user = user
                break

        return updated_user
            

# Delete User
    def delete_user_service(self, id: str, column_index: int = 0):
        rows = []
        with open("user_database.csv", 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if row and len(row) > column_index and row[column_index] == id:
                    continue
                rows.append(row)

        with open('user_database.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for row in rows:
                    writer.writerow(row)

        return {"message": "User Deleted"}

