from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from serializers.signup import SignUp

from repository.database import DatabaseRepo

from use_cases.signup import SignUpUseCase

class Signup(APIView):
    def post(self, request: Request):
        serializer = SignUp(data=request.data)
        serializer.is_valid(raise_exception=True)
        repo = DatabaseRepo()
        uc = SignUpUseCase(repo)
        response = uc.execute(request.data)
        return Response(response, status=201, headers={'Content-Type':'application/json'})