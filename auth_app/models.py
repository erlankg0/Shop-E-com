from django.db import models
from django.contrib.auth.models import AbstractUser


class Phone(models.Model):
    number = models.CharField(
        max_length=40,
        verbose_name='Номер Тел',
        unique=True,
    )

    def __str__(self):
        return self.number


class Country(models.Model):
    name = models.CharField(
        max_length=155,
        unique=True
    )

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    GENDERS = (
        ('М', 'Мужчина'),
        ("Ж", 'Женщина'),
    )
    gender = models.CharField(
        max_length=20,
        verbose_name='Пол',
    )
    email = models.EmailField(
        max_length=256,
        unique=True,
        verbose_name='E-mail',
    )
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
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        help_text='Город - улица - дом/кв'

    )
    phone = models.ManyToManyField(
        Phone,
        related_name='phone'

    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone.name}"
