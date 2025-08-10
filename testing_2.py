from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

user_db = {
    1: {"name": "John Doe", "age": 30},
    2: {"name": "Jane Smith", "age": 25},
    3: {"name": "Alice Johnson", "age": 28}
}


class User(BaseModel):
    name: str
    age: int

@app.put("/users_db/data/update/{user_id}")
def user_update(user_id:int, user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        return {"message": "User updated successfully",user_id: user_id, "user": user_db[user_id]}
    else:
        return {"message": "User not found"}