from abc import ABC, abstractmethod

from domain.model.dto.response.base_response import Base_response
from domain.repository.user_repository import User_repository


class Auth_use_case(ABC):
    @abstractmethod
    def __init__(self, user_repository: User_repository):
        self.user_repository = user_repository

    @abstractmethod
    def login(self, email: str, password: str) -> Base_response:
        raise NotImplemented
