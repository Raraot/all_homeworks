from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    text = Column(String(350))
    tag = Column(String(51))
    created = Column(DateTime, default=datetime.now())

class Phonebook(Base):
    __tablename__ = "phonebooks"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(150), nullable=False)
    phone = Column(String(50))
    email = Column(String(50))
    created = Column(DateTime, default=datetime.now())


# alembic revision --autogenerate -m 'add phonebook55'
# alembic upgrade head


# alembic revision --autogenerate -m 'add column2'
# alembic upgrade head