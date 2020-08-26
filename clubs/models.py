from django.db import models
from django.conf import settings
from utils.constants import payment_choices
# Create your models here.
class Club(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    parent=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='parent',null=True, blank=True)
    grandparent=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='grandparent' ,null=True,blank=True)
    l_child=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='left_Child',null=True,blank=True)
    r_child=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, related_name='right_Child' ,null=True,blank=True)

    def save_grandparent(self):
        try:
            parent_user=Club.objects.get(user=self.parent)
            self.grandparent=parent_user.parent
        except Exception as e:
            print(e)
    
    def __str__(self) -> str:
        return self.user.get_full_name+" club"



def upload_path(instance, filename):
	return '/'.join(['payment', str(instance.club.user.get_short_name), filename])

class ClubPayment(models.Model):
    club=models.ForeignKey(Club, on_delete=models.PROTECT)
    parent_paid=models.CharField(max_length=255,choices=payment_choices, default='unpaid')
    grand_parent_paid=models.CharField(max_length=255,choices=payment_choices, default='unpaid')
    parent_document=models.ImageField(blank=True, null=True,upload_to=upload_path)
    grand_parent_document=models.ImageField(blank=True, null=True,upload_to=upload_path)

    def __str__(self) -> str:
        return self.club.user.email

        