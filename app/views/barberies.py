from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from repository.database import DatabaseRepo

from use_cases.barberies import BarberiesUseCase

class Barberies(APIView):
    def get(self, request: Request):
        repo = DatabaseRepo()
        uc = BarberiesUseCase(repo)
        response = uc.execute(request.query_params.get('City','MDE'))
        return Response(response, status=200, headers={'Content-Type':'application/json'})