from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Doctor
from .forms import DoctorForm


def add_doctor(request):
    template_name = 'dashboard/doctors/add-doctor.html'

    if request.method == 'POST':
        doctor_form = DoctorForm(data=request.POST)

        if doctor_form.is_valid():
            doctor = doctor_form.save(commit=False)
            doctor.save()
            messages.success(
                request, 'Doctor data stored successfully.')
            return redirect('doctors:add-doctor')

    else:
        doctor_form = DoctorForm()

    context = {
        'doctor_form': doctor_form,
    }

    return render(request, template_name, context)


def doctor_list(request):

    template_name = 'dashboard/doctors/doctor-list.html'

    doctors = Doctor.objects.all()

    context = {
        'doctors': doctors,
    }

    return render(request, template_name, context)

