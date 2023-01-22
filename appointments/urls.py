from django.urls import path

from . import views

app_name = 'appointments'

urlpatterns = [
    path('appointments/', views.appointment_list, name='appointment-list'),
    path('add-appointment/', views.add_appointment, name='add-appointment'),
    path('reports/', views.report_list, name='report-list'),
    path('add-report/', views.add_report, name='add-report'),
]
