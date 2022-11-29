from decimal import Decimal
from django.conf import settings
from products.models import Product

"""
Хранение корзины покупок в сессиях
Необходимо создать простую структуру, которая может быть сериализована в JSON для хранения элементов корзины в сессии. Корзина должна включать следующие данные для каждого содержащегося в ней элемента:

id экземпляра Product
Количество товара, выбранное для данного продукта
Цена единицы для данного продукта
"""


class Cart(object):
    def __init__(self, request):
        """
        Инициализация корзины товара
        """
        self.session = request.session  # запоминает текушию сессию (берем из request)
        """
        Пытаемся получить данные корзины
        """
        cart = self.session.get(settings.CART_SESSION_ID)
        """
        Если в корзине имется товара возврашаем
        """
        if not cart:
            """
            сохраняем ПУСТУЮ корзину товаров в сессии
            """
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебираем товары в корзине и получаем товары из базы данныех.

        В методе __iter__() мы извлекаем экземпляры продукта, присутствующие в корзине, чтобы включить
        их в номенклатуры корзины. Наконец, мы проходим по элементам корзины, преобразуя цену номенклатуры
        обратно в десятичное число и добавляя атрибут total_price к каждому элементу. Теперь можно легко выполнить
        итерацию по товарам в корзине.

        Нам также нужен способ вернуть общее количество товаров в корзине. Когда функция len() выполняется на объекте,
        Python вызывает метод __len__() для извлечения ее длины. Мы собираемся определить пользовательский
        метод __len__(), чтобы вернуть общее количество элементов, хранящихся в корзине. Добавьте следующий
        метод __len__() в класс Cart:


        :return:
        """
        product_ids = self.cart.keys()
        # получаем товары и добавляем их в корщину
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине
        :return:
        """

        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.

        Метод add() принимает следующие параметры:

    product : Экземпляр Product для добавления или обновления в корзине
    quantity : Необязательное целое число для количества продукта. По умолчанию используется значение 1 .
    update_quantity : Это логическое значение, которое указывает, требуется ли обновление количества с заданным
    количеством (True), или же новое количество должно быть добавлено к существующему количеству (False).
    id продукта используется в качестве ключа в словаре содержимого корзины. id продукта преобразуется в строку,
    так как Джанго использует JSON для сериализации данных сессии, а JSON разрешает только имена строк.
    id продукта — это ключ, а значение, которое мы сохраняем, — словарь с количеством и ценой для продукта.
    Цена продукта преобразуется из десятичного разделителя в строку, чтобы сериализовать его.
    Наконец, мы вызываем метод save(), чтобы сохранить корзину в сессии.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(product.price)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сесси cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметка сеанс как "измененый", чтобы убедится что он сохраненый
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине
        :return:
        """

        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # Удаление товара из сесси
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
