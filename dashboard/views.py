from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import UserAccount
from appointments.models import Appointment
from doctors.models import Doctor
from departments.models import Department


@login_required(login_url='index:index')
def dashboard(request):
    client_template = 'dashboard/index-client.html'
    admin_template = 'dashboard/index-admin.html'

    template_name = admin_template if request.user.is_admin else client_template



    total_users_count = UserAccount.objects.all().count()
    total_clients_count = UserAccount.objects.filter(is_client=True, is_superuser=False).count()
    total_doctors_count = Doctor.objects.all().count()
    total_departments_count = Department.objects.all().count()
    total_appointments_count = Appointment.objects.all().count()

    appointments = Appointment.objects.all()[:5]
    doctors = Doctor.objects.all()[:10]
    departments = Department.objects.all()[:5]

    client_appointments = Appointment.objects.filter(user=request.user)[:5]
    client_appointments_count = Appointment.objects.filter(user=request.user).count()

    context = {
        'total_users_count': total_users_count,
        'total_clients_count': total_clients_count,
        'total_doctors_count': total_doctors_count,
        'total_departments_count': total_departments_count,
        'total_appointments_count': total_appointments_count,

        'appointments': appointments,
        'doctors': doctors,
        'departments': departments,

        'client_appointments': client_appointments,
        'client_appointments_count': client_appointments_count,
    }

    return render(request, template_name, context)


def clients_list(request):
    template_name = 'dashboard/clients.html'

    clients = UserAccount.objects.filter(
        is_client=True, is_admin=False, is_staff=False, is_superuser=False)
    context = {
        'clients': clients,
    }
    return render(request, template_name, context)


def admins_list(request):
    template_name = 'dashboard/admins.html'

    admins = UserAccount.objects.filter(is_admin=True)
    context = {
        'admins': admins,
    }
    return render(request, template_name, context)
