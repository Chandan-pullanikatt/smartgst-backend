from rest_framework import generics, permissions
from api.models.invoice_models import Invoice
from api.serializers.invoice_serializers import InvoiceSerializer

class InvoiceListCreateView(generics.ListCreateAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return invoices belonging to the logged-in user
        return Invoice.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Attach the logged-in user before saving
        serializer.save(user=self.request.user)
class InvoiceDeleteView(generics.DestroyAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)

