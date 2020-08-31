from .models import UserRegistrationStatusDetails
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender=UserRegistrationStatusDetails)
def registerUser(sender, instance,  created, **kwargs):
    print("in signals")
    if not created:
        user=instance.user
        user.registered=True
        user.save()
    
#post_save.connect(registerUser, sender=UserRegistrationStatusDetails)