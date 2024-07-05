from abc import ABC
from typing import List

from domain.model.dto.response.user_response import User_response
from domain.model.user_domain import User_domain
from domain.repository.user_repository import User_repository
from infraestructure.configuration.db import SessionLocal
from infraestructure.mappers.user_mapper_service import UserMapperService
from infraestructure.schema.models_factory import Users


class User_repository_impl(User_repository, ABC):
    def __init__(self):
        self.db = SessionLocal()

    def add_user(self, user: User_domain):
        user_entity = UserMapperService.to_db(user)
        self.db.add(user_entity)
        self.db.commit()
        self.db.refresh(user_entity)
        self.db.close()
        return UserMapperService.to_entity_db(user_entity)

    def get_all(self) -> List[User_response]:
        users = self.db.query(Users).all()
        return [UserMapperService.to_entity_db(user) for user in users]

    def get_by_id(self, user_id: str) -> User_response:
        return self.db.query(Users).filter(Users.uuid == user_id).first()

    def delete_user(self, user_id: str):
        user = self.db.query(Users).filter(Users.uuid == user_id).first()
        self.db.delete(user)
        self.db.commit()
        self.db.close()

    def update_user(self, user: User_domain, user_id: str):
        user_db = self.db.query(Users).filter(Users.uuid == user_id).first()
        user_db.name = user.name
        user_db.lastname = user.lastname
        user_db.email = user.email
        user_db.password = user.password
        self.db.commit()
        self.db.refresh(user_db)
        self.db.close()
        return UserMapperService.to_entity_db(user_db)

    def get_by_email(self, email: str) -> User_domain:
        return self.db.query(Users).filter(Users.email == email).first()
