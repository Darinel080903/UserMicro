from abc import ABC
from typing import List

from domain.model.dto.response.user_response import User_response
from domain.model.dto.rol import Rol
from domain.model.user_domain import User_domain
from domain.repository.user_repository import User_repository
from infraestructure.configuration.db import SessionLocal
from infraestructure.mappers.user_mapper_service import UserMapperService
from infraestructure.schema.models_factory import Users
import boto3
from botocore.exceptions import NoCredentialsError


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
        self.db.close()
        return [UserMapperService.to_entity_db(user) for user in users]

    def get_by_email(self, user_email: str) -> User_response:
        return self.db.query(Users).filter(Users.email == user_email).first()

    def delete_user(self, user_id: str):
        user = self.db.query(Users).filter(Users.uuid == user_id).first()
        self.db.delete(user)
        self.db.commit()
        self.db.close()

    def update_user(self, user: User_domain, user_id: str):
        user_db = self.db.query(Users).filter(Users.uuid == user_id).first()
        user_db.name = user.name
        user_db.lastname = user.lastname
        user_db.phone_number = user.phone_number
        self.db.commit()
        self.db.refresh(user_db)
        self.db.close()
        return UserMapperService.to_entity_db(user_db)

    def post_image(self, content: bytes, filename: str, bucket: str, s3_filename: str):
        s3 = boto3.client('s3')
        file_extension = filename.rsplit('.', 1)[1].lower()
        content_type = 'image/jpeg' if file_extension in ['jpg', 'jpeg'] else 'image/png'
        s3.put_object(Bucket=bucket, Key=s3_filename, Body=content, ACL='public-read', ContentType=content_type)
        return f"https://{bucket}.s3.amazonaws.com/{s3_filename}"

    def create_image_for_user(self, user_id: str, url: str):
        user = self.db.query(Users).filter(Users.uuid == user_id).first()
        user.profile = url
        self.db.commit()
        self.db.refresh(user)
        self.db.close()

    def get_by_email_login(self, email: str):
        return self.db.query(Users).filter(Users.email == email).first()

    def update_role(self, user_id: str):
        user = self.db.query(Users).filter(Users.uuid == user_id).first()
        user.rol = Rol.ADMIN
        self.db.commit()
        self.db.refresh(user)
        self.db.close()
