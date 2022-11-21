from django.urls import path
from auth_app import views

urlpatterns = [
    path('add/', views.CustomUserFormView.as_view()),
    # AJAX
    path('ajax/load-provinces/', views.load_provinces, name='ajax_load_provinces'),
]
