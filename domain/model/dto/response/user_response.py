class User_response:
    def __init__(self, uuid: str, name: str, lastname: str, email: str):
        self.uuid = uuid
        self.name = name
        self.lastname = lastname
        self.email = email

    def get_uuid(self):
        return self.uuid

    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def get_email(self):
        return self.email

    def set_name(self, name):
        self.name = name

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_email(self, email):
        self.email = email

    def set_uuid(self, uuid):
        self.uuid = uuid

