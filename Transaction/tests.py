from django.test import TestCase
import razorpay
import requests
import json
# Create your tests here.
client = razorpay.Client(auth=("rzp_test_GP7hCrPCLZN5V5", "WaGtzJA3vHOZRAHBAuHM8wbI"))

# resp=client.order.create(amount=5000, currency='INR', payment_capture='1')

# print(resp)

# order_amount = 50000
# order_currency = 'INR'
# order_receipt = 'order_rcptid_11'
# notes = {'Shipping address': 'Bommanahalli, Bangalore'}   # OPTIONAL

# client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='1')

# order_amount = 50000
# order_currency = 'INR'
# order_receipt = 'order_rcptid_11'
# notes = {'Shipping address': 'Bommanahalli, Bangalore'}   # OPTIONAL
# client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='1')

#https://api.razorpay.com/v1/orders

data={
    "amount":51578*100,
  "currency":"INR",
}

resp=requests.post('https://api.razorpay.com/v1/orders', data, auth=("rzp_test_GP7hCrPCLZN5V5", "WaGtzJA3vHOZRAHBAuHM8wbI" ))

print(resp.text)

jsonResp=json.dumps(resp.text)

print(jsonResp)
