from .models import User, Group
from rest_framework import serializers
from company.serializer import CompanySerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name','company', 'createdAt']
