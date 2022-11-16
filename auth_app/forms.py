from django import forms

from auth_app.models import Person


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'country', 'province']

        widgets = forms.TextInput(attrs={
            'class': 'form-control'
        })
