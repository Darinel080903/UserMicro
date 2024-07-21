from abc import ABC


from domain.model.dto.response.base_response import Base_response
from domain.model.dto.response.user_response import User_response
from domain.model.dto.rol import Rol
from domain.model.user_domain import User_domain
from domain.repository.user_repository import User_repository
from domain.use_case.user_use_case import User_use_case
import bcrypt


class User_service(User_use_case, ABC):
    def __init__(self, user_repository: User_repository):
        self.user_repository = user_repository

    def get_all(self) -> Base_response:
        try:
            users = self.user_repository.get_all()
            response = Base_response(data=users, message='Success', code=200)
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()

    def add_user(self, user: User_domain) -> Base_response:
        try:
            if len(user.password) < 8:
                raise Exception('Password must have at least 8 characters')
            hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
            user.password = hashed_password
            user = self.user_repository.add_user(user)
            response = Base_response(data=user, message='Success', code=201)
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()

    def update_user(self, user: User_domain, user_id: str) -> Base_response:
        try:
            user = self.user_repository.update_user(user, user_id)
            response = Base_response(data=user, message='Success', code=200)
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()

    def delete_user(self, user_id: str):
        try:
            self.user_repository.delete_user(user_id)
            response = Base_response(data=None, message='Success', code=200)
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()

    def get_by_email(self, user_email: str) -> Base_response:
        try:
            user = self.user_repository.get_by_email(user_email)
            user = User_response(email=user.email, uuid=user.uuid, name=user.name, lastname=user.lastname, profile=user.profile, phone_number=user.phone_number, role=user.role)
            response = Base_response(data=user, message='Success', code=200)
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()

    def upload_image(self, content: bytes, filename: str, uuid: str) -> Base_response:
        valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
        file_extension = filename.rsplit('.', 1)[1].lower()
        if file_extension not in valid_extensions:
            raise Exception('Invalid file type')

        try:
            url = self.user_repository.post_image(content, filename, 'profileusersestablishment', filename)
            print("waos",url)
            self.user_repository.create_image_for_user(uuid, url)
            response = Base_response(data=None, message='Success', code=201)
            return response.to_dict()
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
            return response.to_dict()

    def update_role(self, user_id: str) -> Base_response:
        try:
            self.user_repository.update_role(user_id)
            response = Base_response(data=None, message='Success', code=200)
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()
