from repository.database import DatabaseRepo

class BarberiesUseCase:
    def __init__(self, database: DatabaseRepo):
        self.__database = database

    def execute(self, city):
        response = self.__database.get_barberies(city)
        return response.to_dict()