from django.contrib import admin
from db.models import Users, Barberies, Barbers, Services, Schedule, Bookings
# Register your models here.

admin.site.register(Users)
admin.site.register(Barberies)
admin.site.register(Barbers)
admin.site.register(Services)
admin.site.register(Schedule)
admin.site.register(Bookings)