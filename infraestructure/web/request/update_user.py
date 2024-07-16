from pydantic import BaseModel


class UpdateUser(BaseModel):
    name: str
    lastname: str
    phone_number: str
