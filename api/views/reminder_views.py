from rest_framework import generics, permissions
from api.models.reminder_models import Reminder
from api.serializers.reminder_serializers import ReminderSerializer


class ReminderListCreateView(generics.ListCreateAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Reminder.objects.filter(user=self.request.user).order_by('due_date')
        business_id = self.request.query_params.get('business')
        if business_id:
            queryset = queryset.filter(business_id=business_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReminderDeleteView(generics.DestroyAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Reminder.objects.filter(user=self.request.user)
        print(f"[DEBUG] Authenticated user: {self.request.user.id} ({self.request.user.username})")
        print(f"[DEBUG] Accessible reminders: {list(qs.values('id', 'title', 'user_id'))}")
        return qs
