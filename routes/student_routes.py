from bson import ObjectId
from fastapi import APIRouter
from models.student_model import Student_model
from config.database import con
import uuid
from schemas.student_Schemas import liststudentEntity, studentEntity
id = uuid.uuid1()
print(id)
print(id.hex)
student_router = APIRouter()


@student_router.get('/students')
async def find_all_student():
    return  liststudentEntity(con.local.student.find())


@student_router.post('/students')
async def create_student(student: Student_model):
    ins = con.local.student.insert_one(dict(student))
    return  studentEntity(con.local.student.find_one({'_id': ObjectId(ins.inserted_id)}))


@student_router.get('/students/{id}')
async def find_student(id):
    return  studentEntity(con.local.student.find_one({'_id': ObjectId(id)}))


@student_router.put('/students/{id}')
async def update_student(id, student: Student_model):
    up_st =  studentEntity(con.local.student.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': dict(student)}
    ))
    print(up_st)
    return studentEntity(con.local.student.find_one({'_id': ObjectId(id)}))


@student_router.delete('/students/{id}')
async def delete_student(id):
    return studentEntity(con.local.student.find_one_and_delete({'_id': ObjectId(id)}))
