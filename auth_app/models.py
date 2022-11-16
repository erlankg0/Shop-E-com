from django.db import models
from django_countries.fields import CountryField


class Country(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
