from enum import auto
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display=('email','mobile','get_full_name','registered','parent_paid','grandparent_paid')
    search_fields=('email','mobile')
    readonly_fields=('date_joined','last_login')
    exclude=('groups','user_permissions')
    filter_horizontal=()
    list_filter=()
    fieldsets=()

class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display=('user','pan','aadhar')
    search_fields=('pan','aadhar')
    autocomplete_fields=('user',)
    readonly_fields=()
    filter_horizontal=()
    list_filter=()
    fieldsets=()

class BankDetailsAdmin(admin.ModelAdmin):
    list_display=('user','account_holder_name','bank_name','branch_name','ifsc_code')
    search_fields=('account_holder_name','bank_name','branch_name','ifsc_code')
    readonly_fields=()
    filter_horizontal=()
    list_filter=()
    fieldsets=()


class PaymentStatusDetailsAdmin(admin.ModelAdmin):
    list_display=('user','payment_status')
    search_fields=('payment_status',)
    autocomplete_fields=('user',)
    readonly_fields=()
    filter_horizontal=()
    list_filter=()
    fieldsets=()




admin.site.register(UserPersonalDetails, PersonalDetailsAdmin)
#admin.site.register(SMS_OTP)
#admin.site.register(EMAIL_OTP)
admin.site.register(UserDetails,AccountAdmin)
admin.site.register(UserBankDetails, BankDetailsAdmin)
admin.site.register(UserRegistrationStatusDetails, PaymentStatusDetailsAdmin)