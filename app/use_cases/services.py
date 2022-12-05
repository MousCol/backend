from repository.database import DatabaseRepo

class ServicesUseCase:
    def __init__(self, database: DatabaseRepo):
        self.__database = database

    def execute(self, barber_id, service_id, date):
        services = self.__database.get_service(service_id)
        return services.to_dict()