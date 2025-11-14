from django.db import models
from api.models.business_models import Business
from django.contrib.auth import get_user_model

User = get_user_model()

class Invoice(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='invoices')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices')
    customer_name = models.CharField(max_length=150)
    customer_gstin = models.CharField(max_length=15, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    gst_rate = models.DecimalField(max_digits=5, decimal_places=2, default=18.0)
    cgst = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    sgst = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    igst = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_interstate = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Auto-calculate GST values and total before saving"""
        gst_amount = (self.amount * self.gst_rate) / 100
        if self.is_interstate:
            self.igst = gst_amount
            self.cgst = 0
            self.sgst = 0
        else:
            self.cgst = gst_amount / 2
            self.sgst = gst_amount / 2
            self.igst = 0
        self.total_amount = self.amount + gst_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice {self.id} - {self.customer_name}"
