from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(docs_url='/')

Students: dict[int, dict] = {}

class StudentRegister(BaseModel):
    id: int = Field(ge=1)
    full_name: str = Field(min_length=3)
    age: int = Field(ge=7)
    email: EmailStr
    password: str = Field(min_length=6)

@app.get("/students")
def read_students():
    return Students

@app.post("/students")
def add_student(data: StudentRegister):
    if data.id in Students:
        return {"error": "Student already exists"}

    Students[data.id] = {
        "full_name": data.full_name,
        "age": data.age,
        "email": data.email,
        "password": data.password ,
    }
@app.put('/update')
def update_product(data:StudentRegister):
    Students[data.id].update({
'full_name': data.full_name,
 'age': data.age,
'email': data.email,
 'password': data.password
})
    return {'message': 'Product updated successfully!'}

@app.delete("/students/{student_id}")
def delete_student(student_id: int = Path(ge=1)):
    if student_id not in Students:
        return {"error": "Student not found"}

    Students.pop(student_id)
    return {"message": "Student deleted successfully"}

