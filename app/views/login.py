from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from serializers.login import LoginSerializer

from repository.database import DatabaseRepo

from use_cases.login import LoginUseCase

class Login(APIView):
    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        repo = DatabaseRepo()
        uc = LoginUseCase(repo)
        response = uc.execute(request.data)
        return Response(response, status=201, headers={'Content-Type':'application/json'})