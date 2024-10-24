from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel


app = FastAPI()
router = APIRouter()

# Dictionary to store user data
users = {}


# Pydantic model for user data
class User(BaseModel):
    name: str
    email: str


# POST request to add a new user
@router.post("/users/")
async def create_user(user: User):
    if user.name in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.name] = user
    return {"message": "User created successfully"}


# GET request to retrieve user data
@router.get("/users/")
async def read_user():
    return users


# Include the router in the main app
app.include_router(router)
