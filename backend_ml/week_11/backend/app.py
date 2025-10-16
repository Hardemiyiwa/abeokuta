from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="simple FastAPI App", version="1.0.0")

@app.get("/", description="This endpoint just return a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI Aplication"}

if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port = int(os.getenv("port")))