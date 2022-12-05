from rest_framework import serializers

class SignUp(serializers.Serializer):
    first_name = serializers.CharField(max_length=80)
    last_name = serializers.CharField(max_length=80)
    email = serializers.CharField(max_length=80)
    password = serializers.CharField(max_length=80)
    phone = serializers.CharField(max_length=15)