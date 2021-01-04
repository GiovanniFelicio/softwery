from .models import Company
from rest_framework import serializers
from user.serializer import UserSerializer

class ListSerializer(serializers.ModelSerializer):
    user_set = UserSerializer(many=True)
    class Meta:
        model = Company
        fields = ['id', 'name', 'active', 'user_set']