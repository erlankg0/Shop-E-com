from django.urls import path
from auth_app import views

urlpatterns = [

    # AJAX
    path('ajax/load-provinces/', views.load_provinces, name='ajax_load_provinces'),
    path('ajax/load-countries/', views.load_countries, name='ajax_load_countries'),
    path('ajax/load_country_with_provinces/', views.load_country_with_provinces,
         name='ajax_load_country_with_provinces'),

]
