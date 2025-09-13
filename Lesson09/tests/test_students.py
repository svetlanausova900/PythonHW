import pytest
from sqlalchemy.exc import IntegrityError
from database import Student

class TestStudentsCRUD:
    #Тест добавления студента
    def test_add_student(self, db_session):
     
        new_student = Student(
            name="Светлана Усова",
            email="usova@gmail.com",
            course="SQL"
        )
        
        db_session.add(new_student)
        db_session.commit()
        
        saved_student = db_session.query(Student).filter_by(email="usova@gmail.com").first()
        assert saved_student is not None
        assert saved_student.name == "Светлана Усова"
        assert saved_student.course == "SQL"        
    

    #Тест изменения данных студента
    def test_update_student(self, db_session):
       

        student = Student(
            name="Петя Пупкин",
            email="petr@gmail.com",
            course="Postman"
        )
        db_session.add(student)
        db_session.commit()
        
        student_to_update = db_session.query(Student).filter_by(email="petr@gmail.com").first()
        student_to_update.course = "Postman"
        db_session.commit()
        
        updated_student = db_session.query(Student).filter_by(email="petr@gmail.com").first()
        assert updated_student.course == "Postman"
        assert updated_student.name == "Петя Пупкин" 
    
    #Тест удаления студента
    def test_delete_student(self, db_session):
    
        student = Student(
            name="Варвара Сидорова",
            email="maria@gmail.com",
            course="Тестирование API"
        )
        db_session.add(student)
        db_session.commit()
        
        assert db_session.query(Student).filter_by(email="maria@gmail.com").first() is not None
        
        student_to_delete = db_session.query(Student).filter_by(email="maria@gmail.com").first()
        db_session.delete(student_to_delete)
        db_session.commit()
        
        deleted_student = db_session.query(Student).filter_by(email="maria@gmail.com").first()
        assert deleted_student is None
    
