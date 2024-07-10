from pydantic import BaseModel


class Login_entity_request(BaseModel):
    email: str
    password: str
