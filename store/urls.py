from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart_view, name='cart_view'),
    path('products/', views.product_list, name='product_list'),
]
