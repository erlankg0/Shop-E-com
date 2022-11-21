from django.urls import path
from auth_app import views

urlpatterns = [
    # path('add/', views.CustomUserFormView.as_view()),
    path('register/', views.UserFormView.as_view()),
    path('login/', views.LoginViewCustomerUser.as_view(), name='login_auth'),
    # AJAX
    path('ajax/load-provinces/', views.load_provinces, name='ajax_load_provinces'),
]
