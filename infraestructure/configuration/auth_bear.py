from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from application.service.auth_service import Auth_service


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=401, detail='Invalid authentication scheme')
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=401, detail='Invalid token')
            return credentials.credentials
        else:
            raise HTTPException(status_code=401, detail='Invalid authorization code')

    @staticmethod
    def verify_jwt(jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = Auth_service.jwt_validate(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
