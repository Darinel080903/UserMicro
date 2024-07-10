from sqlalchemy import String, Column, Table, Integer, ForeignKey, DateTime, Enum
from infraestructure.configuration.db import Base, engine, meta
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'user'
    uuid = Column(String(255), primary_key=True, unique=True)
    name = Column(String(255))
    lastname = Column(String(255))
    phone_number = Column(String(255))
    profile = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))


Base.metadata.create_all(engine)
