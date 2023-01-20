from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Appointment
from .forms import AppointmentForm


def add_appointment(request):
    template_name = 'dashboard/appointments/book-appointment.html'

    if request.method == 'POST':
        appointment_form = AppointmentForm(data=request.POST)

        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(
                request, 'You have booked an appointment successfully.')
            return redirect('appointments:add-appointment')

    else:
        appointment_form = AppointmentForm()

    context = {
        'appointment_form': appointment_form,
    }

    return render(request, template_name, context)


def appointment_list(request):

    template_name = 'dashboard/appointments/appointment-list.html'

    client_appointments = Appointment.objects.filter(user=request.user)
    admin_appointments = Appointment.objects.all()


    context = {
        'client_appointments': client_appointments,
        'admin_appointments': admin_appointments,
    }

    return render(request, template_name, context)

