from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# User-related views
from api.views.user_views import RegisterView, UserProfileView, UpdateProfileView, ChangePasswordView

# Business views
from api.views.business_views import (
    BusinessListCreateView,
    BusinessUpdateView,
    BusinessDeleteView
)

# Invoice views
from api.views.invoice_views import InvoiceListCreateView, InvoiceDeleteView

# Dashboard
from api.views.dashboard_views import DashboardSummaryView

# Reminders
from api.views.reminder_views import ReminderListCreateView, ReminderDeleteView

# Feedback
from api.views.feedback_views import FeedbackCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # 🔐 Authentication
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/user/', UserProfileView.as_view(), name='user-profile'),
    path('auth/update/', UpdateProfileView.as_view(), name='update-profile'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change-password'),

    # 🏢 Business Management
    # 🏢 Business Management (Order matters!)
path('business/<int:pk>/delete/', BusinessDeleteView.as_view(), name='business-delete'),
path('business/<int:pk>/', BusinessUpdateView.as_view(), name='business-update'),
path('business/', BusinessListCreateView.as_view(), name='business-list-create'),


    # 🧾 Invoices
    path('invoices/', InvoiceListCreateView.as_view(), name='invoices'),
    path('invoices/<int:pk>/', InvoiceDeleteView.as_view(), name='delete-invoice'),

    # 📊 Dashboard Summary
    path('dashboard/summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),

    # ⏰ Reminders
    path('reminders/', ReminderListCreateView.as_view(), name='reminders'),
    path('reminders/<int:pk>/', ReminderDeleteView.as_view(), name='delete-reminder'),

    # 💬 Feedback
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)