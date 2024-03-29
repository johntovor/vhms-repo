from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Department
from .forms import DepartmentForm


@login_required(login_url='accounts:signin')
def add_department(request):
    template_name = 'dashboard/departments/add-department.html'

    if request.method == 'POST':
        department_form = DepartmentForm(data=request.POST)

        if department_form.is_valid():
            department = department_form.save(commit=False)
            department.save()
            messages.success(
                request, 'Department data stored successfully.')
            return redirect('departments:add-department')

    else:
        department_form = DepartmentForm()

    context = {
        'department_form': department_form,
    }

    return render(request, template_name, context)


@login_required(login_url='accounts:signin')
def department_list(request):

    template_name = 'dashboard/departments/department-list.html'

    departments = Department.objects.all()

    context = {
        'departments': departments,
    }

    return render(request, template_name, context)
    pass
