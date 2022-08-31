from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'inut_type': 'password'}
    , write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs={
            'password':{'write_only': True}
        }

    # Validaring Password Confirm Password while Registration

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.DjangoValidationError("Password and Confirm Password does'nt match")
        return attrs
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']  

class UserProfileSerializer(serializers.ModelSerializer):
    class  Meta:
        model = User
        fields = ['id', 'email', 'password']  