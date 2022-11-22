from ajax_select import register, LookupChannel
from auth_app.models import Country


@register('countries')
class CountryLookUp(LookupChannel):
    model = Country

    def get_query(self, q, request):
        return self.model.objects.filter(name=q)

    def format_item_display(self, obj):
        return f"<span class='country'>{obj.name}</span>"
