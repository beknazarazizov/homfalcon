from django.contrib import admin
from django.urls import path

from app.auth_views.views import login, register
from app.views import index, product_details, add_product

urlpatterns = [
    path('index/',index,name='index'),
    path('product_details/<int:pk>',product_details,name='product_details'),
    path('add_product/',add_product,name='add_product'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
]