from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="simple FastAPI App", version="1.0.0")

data = [
    {"name": "Sam larry", "Age": 20, "track": "AI Developer"},
    {"name": "Bahubali", "Age": 21, "track": "Backend Developer"},
    {"name": "John Doe", "Age": 22, "track": "Frontend Developer"},
]

class Item(BaseModel):
    name: str = Field(..., example="Perpetual")
    age: int = Field(..., example=25)
    track: str = Field(..., example= "Fullstack Developer")

# class Edit(BaseModel):
#     name: Optional[str]
#     age: Optional[int]
#     track: Optional[str]


@app.get("/", description="This endpoint just return a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI Aplication"}

@app.get("/get-data")
def get_data():
    return data

@app.post("/create-data")
def create_data(req: Item):
    data.append(req.model_dump())
    print(data)
    return {"Message": "Data Recieved", "Data": data}

@app.put("/update-data/{id}")
def update_data(id: int, req: Item):
    data[id] = req.model_dump()
    print(data)
    return {"Message": "Data Received", "Data": data}

# write an endpoint to patch and delete entries from the data variable

@app.patch("/edit-data/{id}")
def edit_data(id: int, req: Edit):
    try:
        data[id].re
        print(data)
        return {"Message": "Data edited", "Data": data}
    except IndexError:
        return {f"Message": "Record not found"}

@app.delete("/delete-data/{id}")
def delete_data(id: int):
    try:
        del data[id]
        print(data)
        return {"Message": "Data Deleted", "Data": data}
    except IndexError:
        return {f"Message": "Record not found"}


if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port = int(os.getenv("port")))