from django.contrib import admin
from kenzie_connect.models import CustomUser, Survey, Penpal
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Survey)
admin.site.register(Penpal)