from pydantic import BaseModel


class User_entity_request(BaseModel):
    name: str
    lastname: str
    phone_number: str
    email: str
    password: str
