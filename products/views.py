from django.shortcuts import render
from django.views.generic.list import ListView

from products.models import Product, Ip


# Метод для получения ip

def get_client_ip(request):
    http_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if http_forwarded_for:
        ip = http_forwarded_for.split(',')[0]
    else:

        ip = request.META.get('REMOTE_ADDR')  # В REMOTE_ADDR значение айпи пользователя
    return ip


class HomeView(ListView):
    template_name = 'products/index.html'
    model = Product


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
