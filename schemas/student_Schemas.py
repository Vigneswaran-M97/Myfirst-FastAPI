def studentEntity(db_item)-> dict:
    return {
        "id":str(db_item['_id']),
        "name":str(db_item['student_name']),
        "email":str(db_item['student_email']),
        "phone":int(db_item['student_phone'])
    }
    
def liststudentEntity(db_list_item)->dict:
    list_student_entity = []
    for item in db_list_item:
        list_student_entity.append(studentEntity(item))
    return list_student_entity