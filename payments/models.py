from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import requests

class InitializePaymentView(APIView):
    def post(self, request):
        email = request.user.email
        amount = request.data.get('amount') # Passed in cents/kobo
        
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }
        
        # Callback URL should point back to your Frontend
        callback_url = "https://your-frontend-domain.vercel.app/testing?payment=success"
        
        data = {
            "email": email,
            "amount": amount,
            "callback_url": callback_url
        }
        
        try:
            resp = requests.post('https://api.paystack.co/transaction/initialize', headers=headers, json=data)
            return Response(resp.json())
        except Exception as e:
            return Response({"status": False, "message": str(e)}, status=500)

class VerifyPaymentView(APIView):
    def get(self, request, reference):
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        }
        resp = requests.get(f'https://api.paystack.co/transaction/verify/{reference}', headers=headers)
        data = resp.json()
        
        if data['status'] and data['data']['status'] == 'success':
            # Logic to grant credits to user can go here
            return Response({"status": "success"})
        return Response({"status": "failed"})
