from django.urls import path

from .views import *





urlpatterns = [
    path("", Home.as_view() , name="home" ),
    path("product", ProductView.as_view() , name="product"),
    path("customer/<int:pk>", CustomerView.as_view(), name="customer"),
    path("order", OrderView.as_view() , name="order")
]
