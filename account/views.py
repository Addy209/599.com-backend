from django.shortcuts import render
import razorpay
# Create your views here.

client = razorpay.Client(auth=("rzp_test_GP7hCrPCLZN5V5", "WaGtzJA3vHOZRAHBAuHM8wbI"))

payment_id = "pay_FRLKN7aCKAZNG"

resp = client.payment.fetch(payment_id)

print(resp)
