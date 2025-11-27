from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.conf import settings

class InitializePaymentView(APIView):
    def post(self, request):
        email = request.user.email
        amount = request.data.get('amount') # In cents/kobo
        
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "email": email,
            "amount": amount,
            "callback_url": "https://applaude.dev/payment/verify" # Frontend URL
        }
        
        resp = requests.post('https://api.paystack.co/transaction/initialize', headers=headers, json=data)
        return Response(resp.json())

class VerifyPaymentView(APIView):
    def get(self, request, reference):
        # Verify with Paystack API
        # ... logic
        return Response({"status": "success"})
