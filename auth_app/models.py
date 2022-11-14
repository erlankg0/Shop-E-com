from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from auth_app.country_list import get_countries, dict_province_by_country


class Country(models.Model):
    name = models.CharField(
        max_length=100,
        choices=get_countries(),
        verbose_name='Выбор страны'
    )

    def __str__(self):
        return self.name


class Province(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name='Выбор страны'

    )

    province = models.CharField(
        max_length=155,
        verbose_name=f'Провинция{country}',
        choices=dict_province_by_country('Kyrgyzstan')
    )


def __unicode__(self):
    return f"{self.country} -> {self.province}"


class User(models.Model):
    first_name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=155,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        max_length=155,
        unique=True,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name='Страна'
    )
    province = ChainedForeignKey(
        Province,
        chained_field='country',
        chained_model_field='country',
        show_all=False,
        auto_choose=True,
        sort=True
    )
