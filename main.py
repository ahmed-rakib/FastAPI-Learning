from fastapi import FastAPI

app = FastAPI()


#single path parameter
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return {"product": product_id}



#multiple path parameter
@app.get("/students/{department}/{student_id}")
async def get_student(department: str, student_id: int):
    return {
        "Department": department,
        "Student Id": student_id
    }


#single Query parameter
@app.get("/users")
async def get_user(id:int):
    return {
        "Id":id,
        "Name": "Rakib",
        "Age": 25
        }


#Multiple query parameter
@app.get("/users/info")
async def get_users(user_id: int, user_name:str):
    return {
        "User Id": user_id,
        "User Name": user_name
    }
    
    
#optional query parameter
from typing import Optional

@app.get("/patient")
async def get_patient(age : Optional[int] = None):
    return {
        "Age": age
    }