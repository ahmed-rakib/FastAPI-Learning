from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str
    age: int


students = []


@app.post("/students")
async def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student Added Successfully",
        "data": student
    }


@app.get("/students")
async def get_students():
    return students


@app.get("/students/{student_id}")
async def get_student(student_id: int):

    for student in students:
        if student.id == student_id:
            return student

    return {"message": "Student Not Found"}


@app.put("/students/{student_id}")
async def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student.id == student_id:
            students[index] = updated_student
            return {
                "message": "Student Updated",
                "student": updated_student
            }

    return {"message": "Student Not Found"}


@app.delete("/students/{student_id}")
async def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student.id == student_id:
            deleted = students.pop(index)

            return {
                "message": "Deleted Successfully",
                "student": deleted
            }

    return {"message": "Student Not Found"}