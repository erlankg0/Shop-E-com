from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import FormView

from auth_app.country_list import province_get_by_country
from auth_app.forms import CustomUserForm, CustomUserFormAuth
from auth_app.models import Country


class LoginViewCustomerUser(LoginView):
    template_name = 'auth_app/login.html'
    form_class = CustomUserFormAuth
    success_url = '/'

    def get_success_url(self):
        return self.success_url


class UserFormView(FormView):
    template_name = 'auth_app/countries.html'
    form_class = CustomUserForm
    success_url = '/success'

    def form_valid(self, form):
        form.save()
        return super(UserFormView, self).form_valid(form)


# class CustomUserFormView(View):
#     form = CustomUserForm
#
#     def get(self, request):
#         print('GET 33333333333333333333333333333333333333333333333333333')
#         return render(request, 'auth_app/register.html', context={"form": self.form})
#
#     def post(self, request):
#         print('POST 3333333333333333333333333333333333333333333333333333334')
#         self.form = self.form(request.POST)
#         if self.form.is_valid():
#             self.form.save()
#             return redirect('/')
#
#         return render(request, 'auth_app/register.html', context={"form": self.form})

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
