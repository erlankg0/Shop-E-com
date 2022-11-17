from django.shortcuts import render
from django_countries import countries

from auth_app.country_list import province_get_by_country
from auth_app.models import Country


# AJAX
def load_countries(request):
    print('LOAD_COUNTRIES')
    return render(request, 'auth_app/countries.html', {'countries': countries.countries.values()})


def load_provinces(request):
    country_id = request.GET.get('country_id')
    print(country_id)
    provinces = province_get_by_country(Country.objects.get(pk=country_id).name)
    return render(request, 'auth_app/province_dropdown_list_option.html', {'provinces': provinces})


def load_country_with_provinces(request):
    if request.GET.get('country_id'):
        provinces = province_get_by_country(Country.objects.get(name=request.GET.get('country_id')))
        return render(request, 'auth_app/province_dropdown_list_option.html',
                      context={"provinces": provinces})
    else:
        return render(request, 'auth_app/countries.html', context={"countries": countries.countries.values()})
