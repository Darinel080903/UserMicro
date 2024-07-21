from pydantic import BaseModel

from domain.model.dto.rol import Rol


class UpdateUser(BaseModel):
    name: str
    lastname: str
    phone_number: str
