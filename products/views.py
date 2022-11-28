from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
from products.models import Product, Ip, Category
from django.http import JsonResponse

"""Попытка получится все категории"""


class Categories:
    def get_categories(self):
        queryset = Category.objects.all()


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
        product = Product.objects.get(slug=self.kwargs['slug'])
        ip = get_client_ip(self.request)

        if Ip.objects.filter(ip=ip).exists():
            product.view.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            product.view.add(Ip.objects.get(ip=ip))
            super(DetailViewProduct, self).get_object(queryset)


# view продуктов по категории
class CategoryProductListView(ListView):
    model = Product
    paginate_by = 1
    context_object_name = 'products'
    template_name = 'products/shop_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.filter(category__slug__contains=self.kwargs['slug'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryProductListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['category_name'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class ShopViewList(ListView):
    """Вывод всех товаров"""
    model = Product
    paginate_by = 1
    context_object_name = 'products'
    template_name = 'products/shop_list.html'


class Search(CategoryProductListView):
    """Поиск товарав по название"""

    def get_queryset(self):
        """ <<Q>> Для комбинации сложных запросов"""
        return Product.objects.filter(
            Q(title__icontains=self.request.GET.get('q')) |
            # поиск по title (не чувствителен к регистру)
            Q(description__icontains=self.request.GET.get('q')) |
            # # поиск по description (не чувствителен к регистру)
            # Q(category__title__icontains=self.request.GET.get('q')) |
            # # поиск по category__title (не чувствителен к регистру)
            Q(brand__title__icontains=self.request.GET.get('q'))
            # поиск по brand__title (не чувствителен к регистру)
        )

    def get_context_data(self, *args, **kwargs):
        context = super(Search, self).get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


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
