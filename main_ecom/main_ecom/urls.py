
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('user.urls')),
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
]
