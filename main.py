# import Enum 
from enum import Enum

from fastapi import FastAPI

# use Enum class to create a subclass with predefined attributes values
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"} 

# define a path parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# declare path operations in order in order of specificity
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/user_id")
async def read_user(user_id: str):
    return {"user_id": user_id}

# path operations cannot be redefined
@app.get("users")
async def read_users():
    return ["Rick", "Morty"]

# this operation never runs.
@app.get("users")
async def read_users():
    return ["Bean", "Elfo"]

# create a path operation using the predefined values
@app.get("models/{model_name}")
async def get_model(model_name: "ModelName"):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name == "lenet":
        return {"model_name": model_name, "message": "LeCNN all images"}

    return {"model_name": model_name, "message": "Have some residuals!"}