from django import forms
from auth_app.models import CustomUser, Phone
from django.forms.models import formset_factory


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['number']


PhoneFormSet = formset_factory(PhoneForm, extra=2, max_num=2, min_num=1)


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
        exclude = [
            'phone'
        ]
        widgets = {

            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'

                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'

                }
            ),
            'gender': forms.Select(
                attrs={
                    "class": 'nice-select w-100',

                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'type': 'tel',
                    'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'country': forms.Select(
                attrs={
                    'class': 'w-100 custom-select',
                    'id': 'country_id',

                }

            ),
            'province': forms.Select(
                attrs={
                    'class': 'custom-select',
                    'id': 'province_id',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
