from django.contrib import admin
from django.urls import path
from .views import CreateOrderNumber


urlpatterns = [
    path('getOrderId/', CreateOrderNumber.as_view()),
    path('getOrderId/<str:pk>', CreateOrderNumber.as_view()),
    
]