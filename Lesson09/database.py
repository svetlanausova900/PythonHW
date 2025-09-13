from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Базовый класс для моделей
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    course = Column(String(50), nullable=False)

# Функция для создания сессии
def create_session():
    DATABASE_URL = "postgresql://postgres:trust@localhost:5432/QA"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()
