from django.test import TestCase
import random

# Create your tests here.
def gen_otp(start,end):
        otp=random.randint(start,end)
        return otp

print(gen_otp(99999,1000000))