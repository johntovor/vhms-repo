from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clients/', views.clients_list, name='clients'),
    path('admins/', views.admins_list, name='admins'),
]
