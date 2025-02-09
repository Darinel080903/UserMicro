from uuid import uuid4

from domain.model.dto.rol import Rol


class User_domain:
    def __init__(self, name: str, lastname: str, phone_number: str, email: str, password: str, rol: Rol):
        self.uuid = str(uuid4())
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        self.profile = ''
        self.email = email
        self.password = password
        self.rol = rol

    def get_id(self):
        return self.uuid

    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_phone_number(self):
        return self.phone_number

    def get_profile(self):
        return self.profile

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_name(self, name):
        self.name = name

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def set_role(self, role):
        self.role = role
