from abc import ABC, abstractmethod
from typing import List

from domain.model.dto.response.base_response import Base_response
from domain.model.dto.response.user_response import User_response
from domain.model.dto.rol import Rol
from domain.model.user_domain import User_domain
from domain.repository.user_repository import User_repository


class User_use_case(ABC):
    @abstractmethod
    def __init__(self, user_repository: User_repository):
        self.user_repository = user_repository

    @abstractmethod
    def get_all(self) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def add_user(self, user: User_domain) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def update_user(self, user: User_domain, user_id: str) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def delete_user(self, user_id: str):
        raise NotImplemented

    @abstractmethod
    def get_by_email(self, user_id: str) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def upload_image(self, content: bytes, filename: str, uuid: str) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def update_role(self, user_id: str) -> Base_response:
        raise NotImplemented
