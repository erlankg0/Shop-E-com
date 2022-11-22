from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_app import models
from auth_app.models import CustomUser

admin.site.register(models.Country)
admin.site.register(models.Phone)
admin.site.register(models.Address)

@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm # Need to learning
    # form = CustomUserChangeForm # Need to learning
    model = CustomUser
    add_fieldsets = (
        *UserAdmin.add_fieldsets, (
            'Custom fields', {
                'fields': (
                    'gender',
                    'phone',
                    'address',
                )
            }
        )
    )
    fieldsets = (
        *UserAdmin.fieldsets, (
            'Custom fields', {
                'fields': (
                    'gender',
                    'phone',
                    'address',
                )
            }
        )
    )
# # admin.site.register(models.CustomUser)
# @admin.register(models.CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     pass
