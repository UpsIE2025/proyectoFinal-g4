from app.basic import get_db
from app.models import Students


def save_student(student):
    with get_db() as db:
        db.merge(student)
        db.commit()
        print("Student saved...")


def delete_student_id(pk):
    with get_db() as db:
        student = db.query(Students).filter(Students.id == pk).first()
        db.delete(student)
        db.commit()
        print("Deleted student...")
