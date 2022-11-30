from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from cart.cart import Cart
from cart.forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """
    Это представление для добавления продуктов в корзину или обновления количества для существующих продуктов.
    Мы используем декоратор require_POST, чтобы разрешить только POST запросы,
    поскольку это представление изменит данные.
    Представление получает ID продукта в качестве параметра. Мы извлекаем экземпляр продукта с заданным ID и
    проверяем CartAddProductForm. Если форма валидна, мы либо добавляем, либо обновляем продукт в корзине.
    Представление перенаправляет по URL-адресу cart_detail, который будет отображать содержимое корзины.
    Мы собираемся создать cart_detail представление в ближайшее время.
    :param request:
    :param product_id:
    :return:
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        card_data = form.changed_data
        cart.add(
            product=product,
            quantity=card_data['quantity'],
            update_quantity=card_data['update']
        )
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """
    Представление cart_remove получает id продукта в качестве параметра. Мы извлекаем экземпляр продукта с заданным id
    удаляем продукт из корзины. Затем мы перенаправляем пользователя на URL-адрес cart_detail.
    :param request:
    :param product_id:
    :return:
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
