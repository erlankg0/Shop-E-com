from django.contrib.auth.models import AbstractUser
from django.db import models


class Phone(models.Model):
    number = models.CharField(
        max_length=40,
        verbose_name='Номер Тел',
        unique=True,
    )

    def __str__(self):
        return self.number


# Auto Write all country from django_countries.fields import countries
# for country in countries.countries.values():
#     country = Country()
#     country.name = country
#     country.save()
#     country = None

class Country(models.Model):
    name = models.CharField(
        max_length=155,
        unique=True
    )

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        verbose_name='Страна',
        related_name='country',
        blank=True,
        null=True,
        default=''
    )
    province = models.CharField(
        max_length=155,
        verbose_name='Область'
    )
    post_code = models.CharField(
        max_length=40,
        verbose_name='Почтовый код',

    )
    city = models.CharField(
        max_length=150,
        verbose_name='Название города'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        help_text='Город - улица - дом/кв',
        default=''

    )

    def save(self, *args, **kwargs):
        self.address = f"{self.country.name} - {self.province} - {self.city} {self.address}"
        return super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return self.address


class CustomUser(AbstractUser):
    GENDERS = (
        ('М', 'Мужчина'),
        ("Ж", 'Женщина'),
    )
    gender = models.CharField(
        max_length=20,
        verbose_name='Пол',
        choices=GENDERS,
    )
    phone = models.CharField(
        max_length=50,
        verbose_name='Номер телефона',
        unique=True,
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.SET_NULL,
        verbose_name='Добавления адреса',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username
