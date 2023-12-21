
from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view() , name='home'),
    path('itemdetails/<slug>/', views.ItemDetailsView.as_view() , name='itemdetailsview'),
    path('ordersummery/', views.OrderSummeryView.as_view() , name='ordersummery'),
    path('add-to-cart/<slug>/',views.add_to_cart,name='cart'),
    path('remove_from_cart/<slug>/',views.remove_from_cart,name='cart-remove'),
    path('remove_single_from_cart/<slug>',views.remove_single_from_cart,name='remove_single_from_cart')
]