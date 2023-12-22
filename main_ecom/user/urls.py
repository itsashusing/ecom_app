
from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.SignUpUserView,name='singuppage'),
    path('checkout/',views.CheckoutView.as_view(),name='checkout'),
]