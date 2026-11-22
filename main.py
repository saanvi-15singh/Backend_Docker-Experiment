from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student Management API")

# Temporary student records
students = [
    {"id": 1, "name": "Saanvi", "course": "CSE"},
    {"id": 2, "name": "Sakshi", "course": "CSE"}
]

# Student data format
class Student(BaseModel):
    name: str
    course: str


# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


# Health check route
@app.get("/health")
def health():
    return {"status": "Application is running"}


# Get all students
@app.get("/students")
def get_students():
    return students


# Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


# Add a new student
@app.post("/students")
def add_student(student: Student):
    new_student = {
        "id": max([s["id"] for s in students], default=0) + 1,
        "name": student.name,
        "course": student.course
    }

    students.append(new_student)
    return new_student


# Update student details
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for student in students:
        if student["id"] == student_id:
            student["name"] = updated_student.name
            student["course"] = updated_student.course
            return student

    raise HTTPException(status_code=404, detail="Student not found")


# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}

    raise HTTPException(status_code=404, detail="Student not found")