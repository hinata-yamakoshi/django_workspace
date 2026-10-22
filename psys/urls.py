from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('CustomerSearch/', views.customer_search, name='customer_search'),
]