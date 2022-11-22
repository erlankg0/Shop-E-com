from django.contrib import admin
from products import models
from django_mptt_admin.admin import DjangoMpttAdmin


@admin.register(models.Age)
class AgeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title", 'parent',)}


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
    list_display = ('title', 'price', )
    prepopulated_fields = {"slug": ('title', 'size', 'category',)}


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ip)
class IpAdmin(admin.ModelAdmin):
    pass
