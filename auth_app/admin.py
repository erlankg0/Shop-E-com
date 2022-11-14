from django.contrib import admin
from auth_app import models


admin.site.register(models.Province)
admin.site.register(models.Country)
admin.site.register(models.User)
# Register your models here.
