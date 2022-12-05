from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=80)
    password = serializers.CharField(max_length=80)