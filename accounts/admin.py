from django.contrib import admin

from .models import UserAccount, SystemAdministrator, Client

admin.site.register([UserAccount, SystemAdministrator, Client])
