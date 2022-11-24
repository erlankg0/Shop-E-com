from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

from auth_app.models import CustomUser
from products.utils import brand_name_directory_path, product_name_directory_path
from products.utils import get_sizes


class Age(models.Model):
    AGE = (
        ("Adult", 'Adult'),
        ("Kids", 'Kids'),
    )
    title = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Возвраст',
        help_text='Для взрослых \n Для детей'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='URL',
        help_text='Уникальное URL'
    )

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Возраст'
        verbose_name_plural = 'Возраст'


class Collection(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Название коллекции',
        unique=True,
    )

    slug = models.SlugField(
        unique=True
    )

    def __str__(self):
        return self.title


class Category(MPTTModel):
    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название категории'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='children',
        blank=True, null=True,
        db_index=True,
        verbose_name='Подкатегория'
    )
    slug = models.SlugField(
        unique=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название бренда'
    )
    slug = models.SlugField(
        unique=True
    )
    image = models.ImageField(
        upload_to=brand_name_directory_path,
        verbose_name='Изображения / Логотип бренда'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Size(models.Model):
    size = models.CharField(
        max_length=10,
        choices=get_sizes()
    )
    count = models.OneToOneField(
        'Quantity',
        related_name='quantity_size',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        unique=True,
    )

    def __str__(self):
        return self.size


class Quantity(models.Model):
    quantity = models.PositiveIntegerField()

    def __int__(self):
        return self.quantity

    def __str__(self):
        return str(self.quantity)


class Ip(models.Model):  # Таблица где будут ip адреса
    ip = models.CharField(
        max_length=46,
        verbose_name='IP'
    )

    def __str__(self):
        return self.ip


class Like(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username


class Product(models.Model):
    image = models.ManyToManyField(
        'Image',
        verbose_name='Изображение продукта',
    )
    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название продукта'
    )
    description = models.TextField(
        max_length=2000,
        verbose_name='Описание продукта'
    )
    article = models.CharField(
        max_length=64,
        blank=False,
        unique=True,
        verbose_name="Артикул",
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Бренд',
        related_name='product_brand'
    )
    category = models.ManyToManyField(
        Category,
        verbose_name='Категория'
    )
    collection = models.OneToOneField(
        Collection,
        on_delete=models.CASCADE,
        verbose_name='Коллекция'
    )
    age_group = models.ManyToManyField(
        Age,
        verbose_name='Возрастная группа'
    )
    price = models.FloatField(
        verbose_name='Цена продукта',
        default=0.0
    )
    discount = models.BooleanField(
        verbose_name='Скидка',
        default=False,
    )
    discount_price = models.FloatField(
        default=0.00
    )
    size = models.ManyToManyField(
        Size,
        verbose_name='Размер',
    )
    sold = models.PositiveIntegerField(
        default=0,
        verbose_name='Проданно',
    )
    view = models.ManyToManyField(
        Ip,
        verbose_name='Ip viewed',
        help_text='Тут будут хранится все ip адреса, которые смотрели продукт',
        blank=True,
        null=True,
    )
    liked = models.ManyToManyField(
        Like,
        verbose_name='Like',
        blank=True,
        null=True,
    )

    publication_date = models.DateField(
        auto_created=True,
        verbose_name='Дата публикации',
    )
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"slug": self.slug})

    def total_views(self):
        return self.view.count()

    def total_like(self):
        return self.liked.count()

    def liked_users(self):
        return self.liked.all()

    def __str__(self):
        return f"{self.title} - {self.brand}"

    def save(self, *args, **kwargs):
        if self.discount:
            self.discount_price = self.price - self.discount_price
        return super(Product, self).save(*args, **kwargs)


class Image(models.Model):
    image = models.ImageField(
        upload_to=product_name_directory_path,
        verbose_name='Логотип'
    )

    def __str__(self):
        return self.image.name
