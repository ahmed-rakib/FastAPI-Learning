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
    
#practice
customer_risk_profile = {
    101:{"Name":"Rakib","Risk":"Low","Score":"0.12"},
    102:{"Name":"Rahat","Risk":"High","Score":"0.25"},
    103:{"Name":"Sakib","Risk":"Medium","Score":"0.18"},
    104:{"Name":"Akib","Risk":"Low","Score":"0.13"}
}

@app.get("/customer/{customer_id}")
async def customer_risk(customer_id: int):
    if customer_id not in customer_risk_profile:
        return {"Error": f"Customer {customer_id} not found."}
    
    profile = customer_risk_profile[customer_id]
    
    return {
        "Customer Id": customer_id,
        "Name": profile["Name"],
        "Risk": profile["Risk"],
        "Score": profile["Score"]
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
    


#Query Parameter Practice

all_customers = [
    {"id":1183,"name":"Rakib","city":"Dhaka","risk":"Low"},
    {"id":1184,"name":"Robi","city":"Mymensingh","risk":"High"},
    {"id":1185,"name":"Hasib","city":"Rajshahi","risk":"Medium"},
    {"id":1186,"name":"Tutul","city":"Rangpur","risk":"Mediom"},
    {"id":1187,"name":"Rahat","city":"Barishal","risk":"Low"},
]

@app.get("/customers")
async def get_customers(city: str, risk: str):

    filtered = [
        customer
        for customer in all_customers
        if customer["city"] == city and customer["risk"] == risk
    ]

    return {
        "city": city,
        "risk": risk,
        "count": len(filtered),
        "results": filtered
    }
    