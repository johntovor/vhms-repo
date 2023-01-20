from django.urls import path

from . import views

app_name = 'departments'

urlpatterns = [
    path('departments/', views.department_list, name='department-list'),
    path('add-department/', views.add_department, name='add-department'),
]
