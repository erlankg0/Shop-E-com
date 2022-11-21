from django.shortcuts import redirect, render
from django.views import View
from django_countries import countries

from auth_app.country_list import province_get_by_country
from auth_app.forms import CustomUserForm, PhoneFormSet
from auth_app.models import Country


class CustomUserFormView(View):
    form = CustomUserForm
    formset = PhoneFormSet

    def get(self, request):
        return render(request, 'auth_app/auth.html', context={"form": self.form, "formset": self.formset})

    def post(self, request):
        self.form = self.form(request.POST)
        if self.form.is_valid():
            self.form.save()
            return redirect('/success')
        return render(request, 'auth_app/auth.html', context={"form": self.form, "formset": self.formset})


# def person(request):
#     phone_form = PhoneForm()
#     person_form = formset_factory(PhoneForm, extra=2)
#     if request.method == 'POST':
#         person_form = PersonForm(request.POST)
#         phone_form = PhoneForm(request.POST)
#         print(phone_form)
#         if person_form.is_valid() and phone_form.is_valid():
#             phone = phone_form.save(commit=False)
#             phone.save()
#             person_ = person_form.save(commit=False)
#             person_.save()
#             person_.phone.add(phone)
#             return redirect('/')
#     return render(request, 'auth_app/home.html', {"phone": phone_form, 'person': person_form})


# AJAX

def load_provinces(request):
    country_id = request.GET.get('country_id')
    provinces = province_get_by_country(Country.objects.get(pk=country_id).name)
    return render(request, 'auth_app/province_dropdown_list_option.html', {'provinces': provinces})
