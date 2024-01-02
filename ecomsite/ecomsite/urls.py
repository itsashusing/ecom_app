

#  PROJECT URLS

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('store.urls')),
    path('', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
