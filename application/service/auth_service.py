from abc import ABC

import bcrypt
import jwt

from domain.model.dto.response.base_response import Base_response
from domain.model.dto.response.jwt_response import Jwt_response
from domain.model.dto.response.user_response import User_response
from domain.repository.user_repository import User_repository
from domain.use_case.auth_use_case import Auth_use_case


class Auth_service(Auth_use_case, ABC):
    def __init__(self, user_repository: User_repository):
        self.user_repository = user_repository

    @staticmethod
    def jwt_generate(username: str, user_id: str, secret_key: str):
        payload = {
            'username': username,
            'user_id': user_id
        }
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token

    @staticmethod
    def jwt_validate(token: str):
        pass

    def login(self, email: str, password: str) -> Base_response:
        try:
            user = self.user_repository.get_by_email_login(email)
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                print(user.profile)
                tok = self.jwt_generate(user.email, user.uuid, 'asicuuibryayuoinrinqr3298470947yriueyruiqyeiruqmeiurynqewirye8qw764893481yimumyrqrq')
                gen_jwt = Jwt_response(email=user.email, token=tok)
                response = Base_response(data=gen_jwt, message='Success', code=200)
            else:
                response = Base_response(data=None, message='User not found', code=404)
        except Exception as e:
            response = Base_response(data=None, message=str(e), code=500)
        return response.to_dict()
