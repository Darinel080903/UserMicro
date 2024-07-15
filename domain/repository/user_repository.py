from abc import ABC, abstractmethod
from typing import List

from domain.model.dto.response.user_response import User_response
from domain.model.user_domain import User_domain


class User_repository(ABC):
    @abstractmethod
    def get_all(self) -> List[User_response]:
        raise NotImplemented

    @abstractmethod
    def add_user(self, user: User_domain) -> User_response:
        raise NotImplemented

    @abstractmethod
    def update_user(self, user: User_domain, user_id: str) -> User_response:
        raise NotImplemented

    @abstractmethod
    def delete_user(self, user_id: str):
        raise NotImplemented

    @abstractmethod
    def get_by_id(self, user_id: str) -> User_response:
        raise NotImplemented

    @abstractmethod
    def get_by_email(self, email: str) -> User_domain:
        raise NotImplemented

    @abstractmethod
    def post_image(self,  content: bytes, filename: str, bucket: str, s3_filename: str) -> str:
        raise NotImplemented

    @abstractmethod
    def create_image_for_user(self, user_id: str, url: str):
        raise NotImplemented
