from fastapi import APIRouter
from application.service.user_service import User_service
from domain.model.dto.response.base_response import Base_response
from infraestructure.repository import user_repository_impl
from infraestructure.mappers.user_mapper_service import UserMapperService
from infraestructure.web.request.login_entity_request import Login_entity_request
from infraestructure.web.request.user_entity_request import User_entity_request

controller = APIRouter()
repository = user_repository_impl.User_repository_impl()
service = User_service(repository)

default_route = '/users/api/v1'


@controller.get(default_route + "/")
def get_users():
    users = service.get_all()
    return users


@controller.post(default_route + "/create/")
def create_user(user: User_entity_request):
    user = UserMapperService.to_request_domain(user)
    user_save = service.add_user(user)
    return user_save


@controller.put(default_route + "/update/{user_id}")
def update_user(user_id: str, user: User_entity_request):
    user = UserMapperService.to_request_domain(user)
    user_save = service.update_user(user, user_id)
    return user_save


@controller.delete(default_route + "/delete/{user_id}")
def delete_user(user_id: str):
    return service.delete_user(user_id)


@controller.post(default_route + "/login")
def login_user(login: Login_entity_request):
    user = service.login(login.email, login.password)
    return user


@controller.get("/health")
def health():
    return {"status": "Ok"}
