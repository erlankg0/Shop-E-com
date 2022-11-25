from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from products import models


@admin.register(models.Age)
class AgeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title", 'parent',)}


@admin.register(models.Collection)
class Collection(admin.ModelAdmin):
    pass


@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Quantity)
class QuantityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)
    prepopulated_fields = {"slug": ('title', 'size', 'category',)}
    fieldsets = (
        ('Название продукта', {
            'fields': ('title', 'description', 'article', 'brand', 'publication_date', 'slug',)
        }),
        ('Категории', {
            'fields': ('category', 'age_group', 'collection', 'image',)
        }),
        ('Цена', {
            'fields': ('price', 'discount_price', 'discount',)
        }),
        ('Размер', {
            'fields': ('size', 'sold',)
        }),
        ('Просмотры и нравится', {
            'fields': ('view',)
        })
    )


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ip)
class IpAdmin(admin.ModelAdmin):
    pass
