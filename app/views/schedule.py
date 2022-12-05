from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from repository.database import DatabaseRepo

from use_cases.schedule import ScheduleUseCase

class Schedule(APIView):
    def get(self, request: Request):
        barber = request.query_params.get('barber')
        service = request.query_params.get('service')
        date = request.query_params.get('date')
        repo = DatabaseRepo()
        uc = ScheduleUseCase(repo)
        response = uc.execute(int(barber), int(service), datetime.strptime(date, '%Y-%m-%d'))
        return Response(response, status=200, headers={'Content-Type':'application/json'})