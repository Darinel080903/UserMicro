from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from application.service.auth_service import Auth_service
from application.service.user_service import User_service
from domain.model.dto.response.base_response import Base_response
from infraestructure.repository import user_repository_impl
from infraestructure.mappers.user_mapper_service import UserMapperService
from infraestructure.web.request.login_entity_request import Login_entity_request
from infraestructure.web.request.update_user import UpdateUser
from infraestructure.web.request.user_entity_request import User_entity_request
from infraestructure.configuration.auth_bear import JWTBearer
from fastapi import UploadFile

controller = APIRouter()
repository = user_repository_impl.User_repository_impl()
service = User_service(repository)
service_auth = Auth_service(repository)

default_route = '/api/v1'


@controller.get(default_route + "/", dependencies=[Depends(JWTBearer())])
def get_users():
    users = service.get_all()
    return users


@controller.post(default_route + "/create/")
def create_user(user: User_entity_request):
    user = UserMapperService.to_request_domain(user)
    user_save = service.add_user(user)
    return user_save


@controller.post(default_route + "/add/image/{user_id}", )
def post_image(user_id: str, file: UploadFile):
    return service.upload_image(file.file.read(), file.filename, user_id)


@controller.get(default_route + "/find/{user_email}", dependencies=[Depends(JWTBearer())])
def get_user_email(user_email: str):
    return service.get_by_email(user_email)


@controller.put(default_route + "/update/{user_id}", dependencies=[Depends(JWTBearer())])
def update_user(user_id: str, user: UpdateUser):
    user = UserMapperService.to_update_request_domain(user)
    user_save = service.update_user(user, user_id)
    return user_save


@controller.delete(default_route + "/delete/{user_id}", dependencies=[Depends(JWTBearer())])
def delete_user(user_id: str):
    return service.delete_user(user_id)


@controller.post(default_route + "/login")
def login_user(login: Login_entity_request):
    user = service_auth.login(login.email, login.password)
    return user


@controller.get(default_route + "/health")
def health():
    return {"status": "Ok"}
