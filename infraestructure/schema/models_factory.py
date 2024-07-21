from sqlalchemy import String, Column, Table, Integer, ForeignKey, DateTime, Enum

from domain.model.dto.rol import Rol
from infraestructure.configuration.db import Base, engine, meta
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'user'
    uuid = Column(String(255), primary_key=True, unique=True)
    name = Column(String(100))
    lastname = Column(String(255))
    phone_number = Column(String(12))
    profile = Column(String(255), nullable=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    rol = Column(Enum(Rol))


Base.metadata.create_all(engine)
