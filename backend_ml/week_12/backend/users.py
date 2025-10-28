from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn
import bcrypt
import jwt

load_dotenv()

app = FastAPI(title="Simple App", version="1.0.0")

class simple(BaseModel):
    name: str = Field(..., example="Sam Larry")
    email: str = Field(..., example= "sam@gmail.com" )
    password: str = Field (..., example= "sam123")
    userType: str = Field(..., examples="STUDY")

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
            INSERT INTO users (name, email, password, userType)
            VALUES (:name, :email, :password, :userType)
    """)
        
        salt = bcrypt.gensalt()
        hashpassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)
        
        db.execute(query, {"name": input.name, "email": input.email, "password": hashpassword, "userType": input.userType})
        db.commit()

        return {"message": "user created successfully",
                "data": {"name": input.name, "email": input.email, "user type": input.userType}}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class LoginRequest(BaseModel):
    email: str = Field(..., examples="sam@email.com")
    password: str = Field(..., examples="sam123")

@app.post("/login")
def login(input: LoginRequest):
    try:
        query = text("""
             SELECT * FROM user WHERE email = :email
        """)
        result = db.execute(query, {"email": input.email}).fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="invalid email or password")
        
        verified_password = bcrypt.checkpw(input.password.encode("utf-8"), result.password.encode('utf-8'))

        if not verified_password:
            raise HTTPException(status_code=404, detail= "Invalid email or password")
        
        return{
            "Message": "Logged in successfully"
        }
    except Exception as e:
        raise HTTPException(status_code= 500, detail = str(e))
    

if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv("host"), port = int(os.getenv("port")))