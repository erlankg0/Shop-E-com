from django.shortcuts import render, redirect, get_object_or_404

from auth_app.country_list import province_get_by_country
from auth_app.forms import PersonCreationForm
from auth_app.models import Person, Country
from django_countries import countries


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'auth_app/home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'auth_app/home.html', {'form': form})


# AJAX
def load_countries(request):
    print('LOAD_COUNTRIES')
    return render(request, 'auth_app/countries.html', {'countries': countries.countries.values()})


def load_provinces(request):
    country_id = request.GET.get('country_id')
    provinces = province_get_by_country(country_id)
    return render(request, 'auth_app/province_dropdown_list_option.html', {'provinces': provinces})


def load_country_with_provinces(request):
    if request.GET.get('country_id'):
        provinces = province_get_by_country(Country.objects.get(name=request.GET.get('country_id')))
        return render(request, 'auth_app/province_dropdown_list_option.html',
                      context={"provinces": provinces})
    else:
        return render(request, 'auth_app/countries.html', context={"countries": countries.countries.values()})
