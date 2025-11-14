from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Import all views cleanly
from api.views.user_views import RegisterView, UserProfileView
from api.views.business_views import BusinessListCreateView
from api.views.invoice_views import InvoiceListCreateView
from api.views.dashboard_views import DashboardSummaryView
from api.views.reminder_views import ReminderListCreateView, ReminderDeleteView
from api.views.feedback_views import FeedbackCreateView
from api.views.business_views import BusinessListCreateView, BusinessDeleteView
from api.views.invoice_views import InvoiceListCreateView, InvoiceDeleteView
from api.views.user_views import UpdateProfileView, ChangePasswordView


urlpatterns = [
    # 🔐 Authentication
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/user/', UserProfileView.as_view(), name='user-profile'),
    path('business/<int:pk>/', BusinessDeleteView.as_view(), name='delete-business'),

    # 🏢 Business
    path('business/', BusinessListCreateView.as_view(), name='business'),

    # 🧾 Invoices
     path('invoices/', InvoiceListCreateView.as_view(), name='invoices'),
    path('invoices/<int:pk>/', InvoiceDeleteView.as_view(), name='delete-invoice'),

    # 📊 Dashboard
    path('dashboard/summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),

    # ⏰ Reminders
    path('reminders/', ReminderListCreateView.as_view(), name='reminders'),
    path('reminders/<int:pk>/', ReminderDeleteView.as_view(), name='delete-reminder'),

    # 💬 Feedback
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),

    path('auth/update/', UpdateProfileView.as_view(), name='update-profile'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
]
