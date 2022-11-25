from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from products.models import Product, Ip


# Метод для получения ip адреса

def get_client_ip(request):
    http_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if http_forwarded_for:
        ip = http_forwarded_for.split(',')[0]
    else:

        ip = request.META.get('REMOTE_ADDR')  # В REMOTE_ADDR значение айпи пользователя
    return ip


# View для главной страницы

class HomeView(ListView):
    template_name = 'products/index.html'
    model = Product


# view вывод продукта по slug (detail)

class DetailViewProduct(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

    def get_object(self, queryset=None):
        product = Product.objects.get(slug=self.model.slug)
        ip = get_client_ip(self.request)

        if Ip.objects.filter(ip=ip).exists():
            product.view.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            product.view.add(Ip.objects.get(ip=ip))
            return super(DetailViewProduct, self).get_object(queryset)


# view продуктов по категории
class CategoryProductListView(ListView):
    model = Product
    context_object_name = 'products_by_category'
    template_name = 'products/by_category.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.filter(category__slug__contains=self.kwargs['slug'])
        return queryset


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)

    ip = get_client_ip(request)
    if Ip.objects.filter(ip=ip).exists():
        product.view.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        product.view.add(Ip.objects.get(ip=ip))
    context = {"product": Product.objects.get(slug=slug)}
    return render(request, 'products/product_detail.html', context=context)
