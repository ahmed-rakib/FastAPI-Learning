from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    id: int
    department: str
    age: int
    

@app.post("/students")
async def create_student(student:Student):
    return student




#practice
class LoanApplication(BaseModel):
    
    age: int
    income: float
    loan_amount: float
    employeementYear: int
    
@app.post("/predict")
async def predict_loan(application: LoanApplication):
    if application.income >= 10000 & application.employeementYear >= 2:
        decision ="Approved"
    else:
        decision = "Rejected"
        
    return {
        "Loan Amount": application.loan_amount,
        "Decision": decision
    }




