import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    course = Column(String(50), nullable=False)

# Создание сессии БД и очистка данных после теста
@pytest.fixture(scope="function")
def db_session():

    DATABASE_URL = "postgresql://postgres:trust@localhost:5432/QA"
    engine = create_engine(DATABASE_URL)
    
# Создаем таблицы если их нет
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
# Очистка после теста
    session.query(Student).delete()
    session.commit()
    session.close()
    
    