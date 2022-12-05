import bcrypt

from conf import settings
from repository.database import DatabaseRepo
from repository.execptions import raise_exception

from domain.user import User

class SignUpUseCase:
    def __init__(self, database: DatabaseRepo):
        self.__database = database

    def execute(self, data):
        user_request = User.from_dict(data)
        password = bcrypt.hashpw(user_request.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user_request.password = password
        self.__database.set_user(user_request)
        return {"status": True}