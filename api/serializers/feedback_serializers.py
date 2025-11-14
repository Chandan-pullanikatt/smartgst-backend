from rest_framework import serializers
from api.models.feedback_models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'subject', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']
