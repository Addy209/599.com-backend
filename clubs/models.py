from django.db import models
from django.conf import settings

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

class Club1000(models.Model):
    member=models.OneToOneField(Club,on_delete=models.PROTECT, related_name='member')

    def __str__(self) -> str:
        return self.member.user.get_full_name

        