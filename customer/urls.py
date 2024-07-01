from django.contrib import admin
from django.urls import path, include

from app.views import add_product
from customer.views import customer_list, add_customer,delete_customer

urlpatterns = [
    path('customer_list/',customer_list,name='customers'),
    path('add_customer/',add_customer,name='add_customer'),
    path('delete_customer/<int:pk>',delete_customer,name='delete_customer'),
    ]