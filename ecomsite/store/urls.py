from django.urls import path
from . import views

urlpatterns = [

    path('', views.home,name='home'),
    path('category/<slug:category_slug>/', views.home,name='category'),
    path('product/<slug:category_slug>/<slug:product_slug>/', views.product_details,name='product_details'),
]