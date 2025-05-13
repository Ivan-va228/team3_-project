from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'nickname', 'first_name', 'last_name', 'is_staff', 'is_active')
