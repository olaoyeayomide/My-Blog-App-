from fastapi import APIRouter, HTTPException
from services.user_service import UserService
from schemas.user_schema import UserRequest, UserCreate, UserUpdate
from uuid import UUID
from typing import List


user_service = UserService()
user_router = APIRouter()

userDB: List[UserRequest] = []

# Create User
@user_router.post("/user")
async def create_user(user_data: UserCreate):
    response = user_service.create_user_service(user_data, userDB)
    userDB.append(response)
    return {"message": "User Created Successfully", "data": response}


# Get User
@user_router.get("/user/{id}")
async def get_user(id: str):
    user = user_service.get_user_service(userDB, id)

    if not user:
        raise HTTPException(status_code=404, detail="Sorry We Are Unable To Find This Blog. Please Try Again")
    else:
        response = {"message": "User Found", "blog": user}
        return response
    # return user


# Edit User
@user_router.put("/edit_user", response_model=UserRequest)
async def edit_user(id: str, update_data: UserUpdate):
    updated_user = user_service.edit_user_service(id, update_data, userDB)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Sorry We Are Unable To Edit This Blog Because It Can't Be Found. Please Try Again")
    return updated_user


# Get Users
@user_router.get("/users/")
async def get_users():
    return userDB


# Delete User
@user_router.delete("/delete_user/{user_id}")
def delete_user(id: str):
    result = user_service.delete_user_service(id)

    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User With ID {id} Has Been Deleted Successfully"}

