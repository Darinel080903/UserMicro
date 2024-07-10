class User_response:
    def __init__(self, uuid: str, name: str, lastname: str, phone_number: str, profile: str, email: str):
        self.uuid = uuid
        self.name = name
        self.phone_number = phone_number
        self.profile = profile
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

    def get_phone_number(self):
        return self.phone_number

    def get_profile(self):
        return self.profile

    def set_profile(self, profile):
        self.profile = profile

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_name(self, name):
        self.name = name

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_email(self, email):
        self.email = email

    def set_uuid(self, uuid):
        self.uuid = uuid

