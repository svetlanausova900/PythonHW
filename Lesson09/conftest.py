import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

@pytest.fixture(scope="function")
def db_session():
    """Фикстура для создания сессии базы данных"""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    # Очистка после теста
    session.query(Student).delete()
    session.commit()
    session.close()
    Base.metadata.drop_all(engine)