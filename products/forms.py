from django import forms
from django.contrib import admin
from products.models import Color, Quantity, Size


class QuantityForm(forms.ModelForm):
    class Meta:
        model = Quantity
        fields = ('quantity',)

        widgets = {
            'quantity': forms.TextInput(
                attrs={
                    'type': 'number'
                }
            )
        }


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ('size', 'count', 'color',)
        widgets = {
            'count': forms.TextInput(
                attrs={
                    'type': 'number',
                }
            )
        }
