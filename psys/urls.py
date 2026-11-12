from django.urls import path
from . import views

app_name = 'psys'

urlpatterns = [
    path('', views.Index, name='Index'),
    path('CustomerSearch/', views.CustomerSearch, name='CustomerSearch'),
    path('CustomerManagementMenu/', views.MainMenu, name='CustomerManagementMenu'),
]