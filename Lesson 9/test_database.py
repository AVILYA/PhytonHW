
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base



# Настройка соединения с базой данных. Замените на ваши данные.
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    deleted = Column(Boolean, default=False)


Base.metadata.create_all(engine)


@pytest.fixture(scope="session")
def session():
    session = Session()
    yield session
    session.close()


def test_add_subject(session):
    new_subject = Subject(name="Математика")
    session.add(new_subject)
    session.commit()

    retrieved_subject = session.query(Subject).filter_by(name="Математика").first()
    assert retrieved_subject is not None
    assert retrieved_subject.name == "Математика"
    
   
    session.execute(text(f"DELETE FROM subjects WHERE id = {retrieved_subject.id}"))
    session.commit()



def test_update_subject(session):
    new_subject = Subject(name="Физика")
    session.add(new_subject)
    session.commit()

    retrieved_subject = session.query(Subject).filter_by(name="Физика").first()
    retrieved_subject.name = "Механика"
    session.commit()

    updated_subject = session.query(Subject).filter_by(name="Механика").first()
    assert updated_subject is not None
    assert updated_subject.name == "Механика"

   
    session.execute(text(f"DELETE FROM subjects WHERE id = {updated_subject.id}"))
    session.commit()



def test_soft_delete_subject(session):
    new_subject = Subject(name="Химия")
    session.add(new_subject)
    session.commit()

    retrieved_subject = session.query(Subject).filter_by(name="Химия").first()
    retrieved_subject.deleted = True
    session.commit()

    deleted_subject = session.query(Subject).filter_by(name="Химия", deleted=True).first()
    assert deleted_subject is not None
    assert deleted_subject.deleted == True

    
    session.execute(text(f"DELETE FROM subjects WHERE id = {deleted_subject.id}"))
    session.commit()
