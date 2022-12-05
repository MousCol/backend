from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from repository.database import DatabaseRepo

from use_cases.services import ServicesUseCase

class Services(APIView):
    def get(self, request: Request):
        barbery = request.query_params.get('barbery')
        barber = request.query_params.get('barber')
        repo = DatabaseRepo()
        uc = ServicesUseCase(repo)
        response = uc.execute(int(barbery), int(barber) if barber else None)
        return Response(response, status=200, headers={'Content-Type':'application/json'})