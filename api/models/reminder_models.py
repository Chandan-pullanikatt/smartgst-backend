from django.db import models
from django.contrib.auth import get_user_model
from api.models.business_models import Business

User = get_user_model()

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reminders")
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="reminders")
    title = models.CharField(max_length=150)
    message = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.business.name}"
