from django.db import models
from django.conf import settings
from utils.constants import payment_choices
from django.db.models.signals import post_save
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
    parent_ss_url=models.URLField(blank=True)
    parent_paid=models.CharField(max_length=255,choices=payment_choices, default='unpaid')
    grandparent_ss_url=models.URLField(blank=True)
    grand_parent_paid=models.CharField(max_length=255,choices=payment_choices, default='unpaid')

    def __str__(self) -> str:
        return self.club.user.email

def checkForBothParentPayment(sender, instance, created, **kwargs):
    print('in club signals')
    user=instance.club.user
    if not created:
        if instance.parent_paid=='paid' and not user.parent_paid:
            user.parent_paid=True
        if instance.grand_parent_paid=='paid' and not user.grandparent_paid:
            user.grandparent_paid=True
        
        if not instance.parent_paid=='paid':
            user.parent_paid=False
        if not instance.grand_parent_paid=='paid':
            user.grandparent_paid=False

        user.save()

post_save.connect(checkForBothParentPayment,sender=ClubPayment)
        