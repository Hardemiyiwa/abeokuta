from database import db
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn
import bcrypt
import jwt
from enum import Enum
from middleware import create_token, verify_token

load_dotenv()

app = FastAPI(title="Simple App", version="1.0.0")

token_time = int(os.getenv("token_time"))

class Gender(str, Enum):
    male = "male"
    female = "female"

class simple(BaseModel):
    name: str = Field(..., json_schema_extra={"example":"Sam Larry"})
    email: str = Field(..., json_schema_extra={"example": "sam@gmail.com"})
    password: str = Field (..., json_schema_extra={"example": "sam123"})
    userType: str = Field(..., json_schema_extra={"example":"STUDY"})
    gender: Gender = Field(..., json_schema_extra={"example":"male"})

@app.post("/signup")
def signUp(input: simple):
    try:
        duplicate_query = text("""
            SELECT * FROM users
            WHERE email = :email
        """)
        existing = db.execute(duplicate_query, {"email": input.email}).fetchone()
        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")
        
        query = text("""
            INSERT INTO users (name, email, password, userType, gender)
            VALUES (:name, :email, :password, :userType, :gender)
    """)
        
        salt = bcrypt.gensalt()
        hashpassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)
        
        db.execute(query, {"name": input.name, "email": input.email, "password": hashpassword, "userType": input.userType, "gender": input.gender})
        db.commit()

        return {"message": "user created successfully",
                "data": {"name": input.name, "email": input.email, "userType": input.userType, "gender": input.gender}}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class LoginRequest(BaseModel):
    email: str = Field(..., json_schema_extra={"example": "sam@email.com"})
    password: str = Field(..., json_schema_extra={"example": "sam123"})

@app.post("/login")
def login(input: LoginRequest):
    try:
        query = text("""
             SELECT * FROM users WHERE email = :email
        """)
        result = db.execute(query, {"email": input.email}).fetchone()

        print("DB result:", result)

        if not result:
            raise HTTPException(status_code=404, detail="invalid email or password")
        
        verified_password = bcrypt.checkpw(input.password.encode("utf-8"), result.password.encode('utf-8'))

        if not verified_password:
            raise HTTPException(status_code=404, detail= "Invalid email or password")
        
        encoded_token = create_token(details ={
            "email": result.email,
            "userType": result.userType
        }, expiry = token_time)
        
        return{
            "Message": "Logged in successfully",
            "token": encoded_token
        }
    except Exception as e:
        raise HTTPException(status_code= 500, detail = str(e))
    
class courseRequest(BaseModel):
    title: str = Field(..., json_schema_extra={"example": "Backend Course"})
    level: str = Field(..., json_schema_extra={"example": "Beginner"})


@app.post("/courses")
def addcourses(input: courseRequest, user_data= Depends(verify_token)):
    try:
        if user_data["userType"] != "admin":
            raise HTTPException(status_code="401", detail="You are not authorized to add a course")
        query = text("""
            INSERT INTO courses (title, level)
            VALUES (:title, :level)
    """)
        
        db.execute(query, {"title": input.title, "level": input.level})
        db.commit()

        return {
            "message": "Course added successfully",
            "data": {
                "title": input.title,
                "level": input.level
            }
        }

    except Exception as e:
        raise HTTPException(status_code= 500, detail= str(e))
    

if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv("host"), port = int(os.getenv("port")))