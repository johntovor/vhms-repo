from django.urls import path

from . import views

app_name = 'doctors'

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor-list'),
    path('add-doctor/', views.add_doctor, name='add-doctor'),
]
