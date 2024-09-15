from django.contrib import admin
from useraccount.models import user_account,user_address
# Register your models here.
admin.site.register(user_account)
admin.site.register(user_address)