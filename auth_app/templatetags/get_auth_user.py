from django import template
from auth_app.models import CustomUser

register = template.Library()


@register.simple_tag()
def get_user():
    return CustomUser.objects.all()
# Does not work Error (django.template.exceptions.TemplateSyntaxError: 'get_auth_user' is not a registered tag library.)
