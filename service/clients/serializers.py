from rest_framework import serializers
from .models import Client
class ClientSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.first_name')
    class Meta:
        model = Client
        fields = ['user', 'user_name', 'company_name', 'full_address']


