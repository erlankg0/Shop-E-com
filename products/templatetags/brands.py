from django import template
from products.models import Brand

register = template.Library()


@register.simple_tag()
def get_brands():
    return Brand.objects.all()
