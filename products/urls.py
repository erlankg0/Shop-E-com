from django.urls import path

from products.views import DetailViewProduct, HomeView, CategoryProductListView, Search, ShopViewList
from products.views import product_detail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopViewList.as_view(), name='shop'),
    path('product/search/', Search.as_view(), name='search'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('product/category/<slug:slug>/', CategoryProductListView.as_view(), name='get_by_category'),

]
