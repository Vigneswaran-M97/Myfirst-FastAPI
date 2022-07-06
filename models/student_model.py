from pydantic import BaseModel

class Student_model(BaseModel):
    student_name: str
    student_email: str
    student_phone: int
    