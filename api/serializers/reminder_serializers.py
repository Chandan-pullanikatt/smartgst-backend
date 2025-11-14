from rest_framework import serializers
from api.models.reminder_models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(source="business.name", read_only=True)

    class Meta:
        model = Reminder
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']
