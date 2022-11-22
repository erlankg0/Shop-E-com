from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('s/', include('django.contrib.auth.urls')),
                  path('', include('products.urls')),
                  path('auth/', include('auth_app.urls')),
                  path('chaining/', include('smart_selects.urls')),
                  path('ajax-select/', include('ajax_select.urls')),  # AJAX select
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
