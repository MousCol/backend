from datetime import datetime, time, timedelta

from conf import settings

from repository.database import DatabaseRepo

def is_time_between(begin_time, end_time, check_time):
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:
        return check_time >= begin_time or check_time <= end_time

def is_time_between_include(begin_time, end_time, check_time):
    if begin_time < end_time:
        return check_time > begin_time and check_time < end_time
    else:
        return check_time > begin_time or check_time < end_time

class ScheduleUseCase:
    def __init__(self, database: DatabaseRepo):
        self.__database = database

    def execute(self, barber_id, service_id, date : datetime):
        service = self.__database.get_service(service_id)
        bookings = self.__database.get_bookings(barber_id, date)
        schedules = self.__database.get_schedule(barber_id, settings.WEEKDAYS[date.weekday()])
        response = {"data": []}
        for i in range(0,60*24,15):
            start_time = time(hour=int(i/60), minute=int(i % 60))
            end_time = (datetime(year=1, month=1, day=1, hour=int(i/60), minute=int(i % 60)) + timedelta(hours=service.span.hour, minutes=service.span.minute)).time()
            flag_schedule = False
            flag_booking = True
            print(start_time, end_time)
            for schedule in schedules.data:
                if is_time_between(schedule.start, schedule.end, start_time) and is_time_between(schedule.start, schedule.end, end_time):
                    flag_schedule = True
            for booking in bookings.data:
                print(is_time_between(booking.start.time(), booking.end.time(), start_time))
                print(is_time_between(booking.start.time(), booking.end.time(), end_time))
                if is_time_between_include(booking.start.time(), booking.end.time(), start_time) or is_time_between_include(booking.start.time(), booking.end.time(), end_time):
                    flag_booking = False                
            if flag_schedule and flag_booking:
                response["data"].append({
                    "start":start_time,
                    "end":end_time,
                })
        return response