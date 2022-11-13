from django.urls import path
from products.views import product_detail, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<str:slug>/', product_detail, name='product_detail'),

]
