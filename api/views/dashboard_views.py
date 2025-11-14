from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.models.invoice_models import Invoice

class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        invoices = Invoice.objects.filter(business__owner=user)

        total_sales = sum(i.amount for i in invoices)
        total_gst = sum((i.cgst + i.sgst + i.igst) for i in invoices)
        total_invoices = invoices.count()
        avg_invoice_value = total_sales / total_invoices if total_invoices > 0 else 0

        return Response({
            "total_sales": total_sales,
            "total_gst_collected": total_gst,
            "total_invoices": total_invoices,
            "average_invoice_value": avg_invoice_value,
        })
