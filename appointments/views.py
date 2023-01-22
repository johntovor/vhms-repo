from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Appointment, DiagnosticReport
from .forms import AppointmentForm, DiagnosticReportForm


@login_required(login_url='accounts:signin')
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


@login_required(login_url='accounts:signin')
def appointment_list(request):

    template_name = 'dashboard/appointments/appointment-list.html'

    client_appointments = Appointment.objects.filter(user=request.user)
    admin_appointments = Appointment.objects.all()


    context = {
        'client_appointments': client_appointments,
        'admin_appointments': admin_appointments,
    }

    return render(request, template_name, context)



@login_required(login_url='accounts:signin')
def add_report(request):
    template_name = 'dashboard/appointments/diagnostic-report.html'

    if request.method == 'POST':
        report_form = DiagnosticReportForm(data=request.POST)

        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.user = request.user
            report.save()
            messages.success(
                request, 'You have added a diagnostic report successfully.')
            return redirect('appointments:add-report')

    else:
        report_form = DiagnosticReportForm()

    context = {
        'report_form': report_form,
    }

    return render(request, template_name, context)


@login_required(login_url='accounts:signin')
def report_list(request):

    template_name = 'dashboard/appointments/report-list.html'

    client_reports = DiagnosticReport.objects.filter(user=request.user)
    admin_reports = DiagnosticReport.objects.all()


    context = {
        'client_reports': client_reports,
        'admin_reports': admin_reports,
    }

    return render(request, template_name, context)

