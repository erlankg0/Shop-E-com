from django.urls import path
from products.views import product_detail, HomeView, CategoryProductListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<str:slug>/', product_detail, name='product_detail'),
    path('product/category/<slug:slug>/', CategoryProductListView.as_view(), name='get_by_category'),

]
