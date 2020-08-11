from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    exclude = ('groups', 'user_permissions')

admin.site.register(UserPersonalDetails)
admin.site.register(SMS_OTP)
admin.site.register(EMAIL_OTP)
admin.site.register(UserDetails,UserAdmin)