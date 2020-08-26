from django.conf import settings
from django.db import models

# Create your models here.

class TransactionDetails(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    order_number=models.CharField(max_length=255, primary_key=True)
    amount=models.IntegerField()
    payment_id=models.CharField(max_length=255, blank=True,unique=True)
    status=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.order_number+ str(self.amount)
