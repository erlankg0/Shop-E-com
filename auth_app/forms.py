from django import forms
from django.forms.models import formset_factory
from django.utils.timezone import now
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from auth_app.models import CustomUser, Phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['number']


PhoneFormSet = formset_factory(PhoneForm, extra=2, max_num=2, min_num=1)


class CustomUserFormAuth(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password',)


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'gender',
            'phone',
            'country',
            'province',
            'city',
            'post_code',
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
                    'type': 'number',
                    'class': 'form-control',
                    'min': '0',
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
            'post_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number',
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'address',
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
            'date_joined': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'value': now,
                    'readonly': '',

                }
            )
        }

    def save(self, commit=True):
        custom_user = super().save(commit=False)
        custom_user.set_password(self.cleaned_data['password'])
        if commit:
            custom_user.save()
        return custom_user
