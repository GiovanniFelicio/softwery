from .models import Company
from rest_framework import serializers
# from user.serializer import UserSerializer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'active']
