from django.contrib import admin
from django.contrib.auth import get_user_model
from api.models.business_models import Business
from api.models.invoice_models import Invoice
from api.models.reminder_models import Reminder
from api.models.feedback_models import Feedback

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_superuser', 'is_staff')
    search_fields = ('username', 'email')

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gstin', 'owner', 'created_at')
    search_fields = ('name', 'gstin', 'owner__username')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'business', 'customer_name', 'amount', 'gst_rate', 'total_amount', 'created_at')
    list_filter = ('business',)
    search_fields = ('customer_name', 'business__name')

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'business', 'title', 'due_date', 'is_done')
    list_filter = ('is_done', 'due_date')
    search_fields = ('title', 'business__name')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'created_at')
    search_fields = ('user__username', 'subject', 'message')
