import imp
from fastapi import FastAPI
from routes.student_routes import student_router

app = FastAPI()

app.include_router(student_router)