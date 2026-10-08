from django.urls import path
from . import views

urlpatterns = [
    path('CustomerSearch/', views.customer_search, name='customer_search'),
]