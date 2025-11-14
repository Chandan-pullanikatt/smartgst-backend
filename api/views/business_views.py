from rest_framework import generics, permissions
from api.models.business_models import Business
from api.serializers.business_serializers import BusinessSerializer

class BusinessListCreateView(generics.ListCreateAPIView):
    serializer_class = BusinessSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Business.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class BusinessDeleteView(generics.DestroyAPIView):
    serializer_class = BusinessSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Business.objects.all()
