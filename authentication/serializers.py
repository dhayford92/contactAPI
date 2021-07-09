from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=225, min_length=4)
    first_name = serializers.CharField(max_length=65, min_length=2)
    last_name = serializers.CharField(max_length=65, min_length=2)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email', ('Email is already in used')})
        return super().validate(attrs)

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=65, min_length=2)
    password = serializers.CharField(max_length=65, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']