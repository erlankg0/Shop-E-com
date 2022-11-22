from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('s/', include('django.contrib.auth.urls')),
                  path('', include('products.urls')),
                  path('auth/', include('auth_app.urls')),
                  path('chaining/', include('smart_selects.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
