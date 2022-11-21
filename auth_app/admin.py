from django.contrib import admin
from auth_app import models

admin.site.register(models.Country)
admin.site.register(models.Phone)


# admin.site.register(models.CustomUser)
@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = [
        'first_name',
        'last_name',
        'email',
        'gender',
        'country',
        'province',
        'address',
        'phone',
        'username',
        'password',
        'is_active',
        'is_staff',
        'is_superuser',
        'user_permissions',
        'groups',
        'last_login',
        'date_joined',
    ]
