from rest_framework import generics, permissions
from api.models.feedback_models import Feedback
from api.serializers.feedback_serializers import FeedbackSerializer

class FeedbackCreateView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Feedback.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
