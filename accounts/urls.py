from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/register-client/',
         views.register_client, name='register-client'),
    path('accounts/register-admin/',
         views.register_admin, name='register-admin'),
    path('accounts/signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('admin-profile/', views.admin_profile, name='admin-profile'),
    path('client-profile/', views.client_profile, name='client-profile'),
]
