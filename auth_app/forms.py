from django import forms
from auth_app.models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
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
