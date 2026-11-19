from django.urls import path
from . import views

app_name = 'psys'

urlpatterns = [
    path('', views.Index, name='Index'),
    path('Login/', views.login, name='Login'),
    path('Logout/', views.logout, name='Logout'),
    path('MainMenu/', views.MainMenu, name='MainMenu'),
    path('CustomerSearch/', views.CustomerSearch, name='CustomerSearch'),
    path('CustomerManagementMenu/', views.CustomerManagementMenu, name='CustomerManagementMenu'),
]