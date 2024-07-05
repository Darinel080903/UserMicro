from domain.model.dto.response.user_response import User_response
from domain.model.user_domain import User_domain
from infraestructure.schema.models_factory import Users
from infraestructure.web.request.user_entity_request import User_entity_request


class UserMapperService:
    @staticmethod
    def to_domain(user: User_entity_request) -> User_domain:
        return User_domain(
            name=user.name,
            lastname=user.lastname,
            email=user.email,
            password=user.password
        )

    @staticmethod
    def to_response(user: User_domain) -> User_response:
        return User_response(
            uuid=user.uuid,
            name=user.name,
            lastname=user.lastname,
            email=user.email,
        )

    @staticmethod
    def to_db(user: User_domain) -> Users:
        return Users(
            uuid=user.uuid,
            name=user.name,
            lastname=user.lastname,
            email=user.email,
            password=user.password
        )

    @staticmethod
    def to_entity_db(user: Users) -> User_response:
        return User_response(
            uuid=user.uuid,
            name=user.name,
            lastname=user.lastname,
            email=user.email,
        )

    @staticmethod
    def to_request_domain(user: User_entity_request) -> User_domain:
        return User_domain(
            name=user.name,
            lastname=user.lastname,
            email=user.email,
            password=user.password
        )
