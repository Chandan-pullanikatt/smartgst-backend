from rest_framework import serializers
from api.models.business_models import Business

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'name', 'gstin', 'address', 'state', 'created_at']
        read_only_fields = ['id', 'created_at']
