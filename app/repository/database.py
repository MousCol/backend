from django.db.utils import IntegrityError
from typing import List
from datetime import timedelta

from repository.execptions import raise_exception

from db.models import *

from domain.user import User
from domain.barberies import BarberiesList
from domain.barbers import BarbersList, Service
from domain.services import ServicesList
from domain.bookings import BookingsList
from domain.schedule import ScheduleList

class DatabaseRepo:
        
    def get_user(self, email) -> Users:
        user = Users.objects.filter(email=email).all()
        if not user: raise_exception("Datos Erroneos")
        return User.from_dict(user[0].__dict__)

    def set_user(self, user: User):
        set_user = Users(
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            phone=user.phone
        )
        try:
            set_user.save()
        except IntegrityError:
            raise_exception("Tu email ya se encuentra registrado")
        return

    def get_barberies(self, city) -> BarberiesList:
        barberies = Barberies.objects.filter(city=city).all()
        if not barberies: raise_exception("Datos Erroneos")
        return BarberiesList.from_dict({
            'data': [barbery.__dict__ for barbery in barberies]
        })

    def get_barbers(self, barbery_id) -> BarberiesList:
        barbers = Barbers.objects.filter(barbery_id=barbery_id).all()
        if not barbers: raise_exception("Datos Erroneos")
        return BarbersList.from_dict({
            'data': [barber.__dict__ for barber in barbers]
        })

    def get_service(self, service) -> Service:
        services = Services.objects.filter(id=service).all()
        if not services: raise_exception("Datos Erroneos")
        return Service.from_dict(services[0].__dict__)

    def get_services(self, barbers) -> ServicesList:
        services = Services.objects.filter(barber_id__in=barbers).all()
        if not services: raise_exception("Datos Erroneos")
        return ServicesList.from_dict({
            'data': [service.__dict__ for service in services]
        })
    
    def get_bookings(self, barber, date) -> BookingsList:
        services = Bookings.objects.filter(barber_id=barber, start__range=[date, date + timedelta(days=1)]).all()
        return BookingsList.from_dict({
            'data': [service.__dict__ for service in services]
        })

    def get_schedule(self, barber, day) -> ScheduleList:
        schedules = Schedule.objects.filter(barber_id=barber, day=day).all()
        if not schedules: raise_exception("Tu barbero no está disponible para esta fecha")
        return ScheduleList.from_dict({
            'data': [schedule.__dict__ for schedule in schedules]
        })
