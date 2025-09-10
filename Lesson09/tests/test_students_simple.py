import pytest
from sqlalchemy.exc import IntegrityError
from models import Student

@pytest.fixture(autouse=True)
def cleanup_test_data(db_session):
    """Автоматическая очистка тестовых данных перед каждым тестом"""
    yield
    # Дополнительная очистка (основная делается в db_session)
    db_session.rollback()

def test_add_student(db_session):
    """Тест добавления студента"""
    # Подготовка данных
    test_student = Student(
        name="Алексей Смирнов",
        email="smirnov@example.com",
        age=21
    )
    
    # Выполнение действия
    db_session.add(test_student)
    db_session.commit()
    
    # Проверка результата
    student_from_db = db_session.query(Student).filter_by(email="smirnov@example.com").first()
    
    assert student_from_db is not None
    assert student_from_db.name == "Алексей Смирнов"
    assert student_from_db.email == "smirnov@example.com"
    assert student_from_db.age == 21

def test_update_student(db_session):
    """Тест изменения данных студента"""
    # Создаем студента для изменения
    student = Student(
        name="Екатерина Иванова",
        email="ivanova@example.com",
        age=22
    )
    db_session.add(student)
    db_session.commit()
    
    # Изменяем данные
    student_to_update = db_session.query(Student).filter_by(email="ivanova@example.com").first()
    student_to_update.name = "Екатерина Петрова"
    student_to_update.age = 23
    db_session.commit()
    
    # Проверяем изменения
    updated_student = db_session.query(Student).filter_by(email="ivanova@example.com").first()
    
    assert updated_student.name == "Екатерина Петрова"
    assert updated_student.age == 23
    assert updated_student.email == "ivanova@example.com"

def test_delete_student(db_session):
    """Тест удаления студента"""
    # Создаем студента для удаления
    student = Student(
        name="Дмитрий Козлов",
        email="kozlov@example.com",
        age=24
    )
    db_session.add(student)
    db_session.commit()
    
    # Проверяем, что студент создан
    student_exists = db_session.query(Student).filter_by(email="kozlov@example.com").first()
    assert student_exists is not None
    
    # Удаляем студента
    student_to_delete = db_session.query(Student).filter_by(email="kozlov@example.com").first()
    db_session.delete(student_to_delete)
    db_session.commit()
    
    # Проверяем, что студент удален
    student_deleted = db_session.query(Student).filter_by(email="kozlov@example.com").first()
    assert student_deleted is None

def test_student_email_uniqueness(db_session):
    """Дополнительный тест: проверка уникальности email"""
    # Создаем первого студента
    student1 = Student(
        name="Ольга Новикова",
        email="novikova@example.com",
        age=20
    )
    db_session.add(student1)
    db_session.commit()
    
    # Пытаемся создать второго студента с таким же email
    student2 = Student(
        name="Ирина Новикова",
        email="novikova@example.com",  # Дубликат email
        age=21
    )
    db_session.add(student2)
    
    # Ожидаем ошибку уникальности
    with pytest.raises(IntegrityError):
        db_session.commit()
    
    # Откатываем несохраненные изменения
    db_session.rollback()
    