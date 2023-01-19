from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import UserAccount


@login_required(login_url='index:index')
def dashboard(request):
    client_template = 'dashboard/index-client.html'
    admin_template = 'dashboard/index-admin.html'

    template_name = admin_template if request.user.is_admin else client_template



    total_users_count = UserAccount.objects.all().count()


    context = {
        'total_users_count': total_users_count,

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
