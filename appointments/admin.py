from django.contrib import admin

from .models import Appointment, DiagnosticReport

admin.site.register([Appointment, DiagnosticReport])
