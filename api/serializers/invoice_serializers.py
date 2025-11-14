from rest_framework import serializers
from api.models.invoice_models import Invoice
from api.utils.gst_calculator import calculate_gst

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            'id', 'business', 'customer_name', 'customer_gstin',
            'amount', 'gst_rate', 'cgst', 'sgst', 'igst',
            'total_amount', 'is_interstate', 'created_at'
        ]
        read_only_fields = ['id', 'cgst', 'sgst', 'igst', 'total_amount', 'created_at']

    def create(self, validated_data):
        amount = validated_data['amount']
        gst_rate = validated_data.get('gst_rate', 18.0)
        is_interstate = validated_data.get('is_interstate', False)

        gst_data = calculate_gst(amount, gst_rate, is_interstate)
        validated_data['cgst'] = gst_data['cgst']
        validated_data['sgst'] = gst_data['sgst']
        validated_data['igst'] = gst_data['igst']
        validated_data['total_amount'] = gst_data['total']

        return super().create(validated_data)
