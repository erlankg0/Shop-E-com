from products.models import Product
from django.shortcuts import render
from django.views.generic.list import ListView


class HomeView(ListView):
    template_name = 'products/index.html'
    model = Product


def product_detail(request, slug):
    context = {"product": Product.objects.get(slug=slug)}
    return render(request, 'products/product_detail.html', context=context)
