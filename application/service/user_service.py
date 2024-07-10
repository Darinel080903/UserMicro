from abc import ABC

from domain.model.dto.response.base_response import Base_response
from domain.model.dto.response.user_response import User_response
from domain.model.user_domain import User_domain
from domain.repository.user_repository import User_repository
from domain.use_case.user_use_case import User_use_case
import bcrypt
import base64


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
            self.base64_to_file(user.profile, 'output.jpg')
            user.profile = self.user_repository.post_image('output.jpg', 'profileusersestablishment', 'output.jpg')
            user = self.user_repository.add_user(user)
            response = Base_response(data=user, message='User created', code=201)

        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()

    def update_user(self, user: User_domain, user_id: str) -> Base_response:
        try:
            hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
            user.password = hashed_password
            user = self.user_repository.update_user(user, user_id)
            response = Base_response(data=user, message='User updated', code=200)
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()

    def delete_user(self, user_id: str):
        try:
            self.user_repository.delete_user(user_id)
            response = Base_response(data=None, message='User deleted', code=200)
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()

    def get_by_id(self, user_id: str) -> User_response:
        return self.user_repository.get_by_id(user_id)

    def login(self, email: str, password: str) -> Base_response:
        try:
            user = self.user_repository.get_by_email(email)
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                user = User_response(uuid=user.uuid, name=user.name, lastname=user.lastname, email=user.email)
                response = Base_response(data=user, message='User found', code=200)
            else:
                response = Base_response(data=None, message='User not found', code=404)
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()

    @staticmethod
    def base64_to_file(base64_string, output_file):
        with open(output_file, 'wb') as file:
            file.write(base64.b64decode(base64_string))


