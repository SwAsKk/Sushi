from unicodedata import name
from urllib.parse import urlparse
from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path(r'add/<int:product_id>/', views.cart_add, name='cart_add'),
    path(r'remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
