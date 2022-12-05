import jwt
import bcrypt
from datetime import datetime,timedelta

from conf import settings
from repository.database import DatabaseRepo
from repository.execptions import raise_exception

from domain.login import Login

class LoginUseCase:
    def __init__(self, database: DatabaseRepo):
        self.__database = database

    def execute(self, data):
        user_request = Login.from_dict(data)
        user = self.__database.get_user(user_request.email)
        if not user.status: 
            raise_exception("Usuario no activo")
        if bcrypt.checkpw(user_request.password.encode('utf-8'), user.password.encode('utf-8')):
            token = jwt.encode({"id": user.id, "type": "authorization", "exp": datetime.now() + timedelta(hours=24)}, settings.SECRET_KEY, algorithm="HS256")
            refresh = jwt.encode({"id": user.id, "type": "authorization", "exp": datetime.now() + timedelta(hours=24)}, settings.SECRET_KEY, algorithm="HS256")
        else: 
            raise_exception("Contraseña invalida")
        return {"token": token, "refresh": refresh}