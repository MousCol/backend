from django.db import models

import datetime

CITIES = [
    ('MDE', 'Medellín'),
]

ROLES = [
    ('ADM', 'Administrador'),
    ('IND', 'Independiente'),
    ('EMP', 'Empleado'),
]

class Barberies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    stars = models.FloatField()
    url = models.CharField(max_length=150)
    longitude = models.FloatField()
    latitude = models.FloatField()
    city = models.CharField(max_length=3, choices=CITIES)
    status = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title

class Barbers(models.Model):
    id = models.AutoField(primary_key=True)
    barbery_id = models.ForeignKey(Barberies, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=80, null=True)
    last_name = models.CharField(max_length=80, null=True)
    stars = models.FloatField()
    url = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=80)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80)
    role = models.CharField(max_length=3, choices=ROLES)
    status = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    barber_id = models.ForeignKey(Barbers, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    cost = models.FloatField()   
    span = models.TimeField()

    def __str__(self):
        return self.name

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80)
    phone = models.CharField(max_length=15)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    barber_id = models.ForeignKey(Barbers, on_delete=models.CASCADE)
    day = models.CharField(max_length=2)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return self.start.strftime("%H:%M")

class Bookings(models.Model):
    id = models.AutoField(primary_key=True)
    barber_id = models.ForeignKey(Barbers, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.start.strftime("%d/%m/%Y %H:%M:")