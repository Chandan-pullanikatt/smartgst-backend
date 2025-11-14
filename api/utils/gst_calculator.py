def calculate_gst(amount, gst_rate, is_interstate=False):
    gst_total = (amount * gst_rate) / 100
    if is_interstate:
        return {
            'igst': gst_total,
            'cgst': 0,
            'sgst': 0,
            'total': amount + gst_total
        }
    else:
        half = gst_total / 2
        return {
            'igst': 0,
            'cgst': half,
            'sgst': half,
            'total': amount + gst_total
        }
