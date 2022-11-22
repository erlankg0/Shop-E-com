from django.urls import path
from auth_app import views

urlpatterns = [
    path('signup/', views.SingUpView.as_view(), name='signup_auth'),
    path('login/', views.LoginViewCustomerUser.as_view(), name='login_auth'),
    # AJAX
    path('ajax/load-provinces/', views.load_provinces, name='ajax_load_provinces'),
]
