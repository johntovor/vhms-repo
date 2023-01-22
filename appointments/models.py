from django.db import models
from django.db.models.signals import pre_save
from phonenumber_field.modelfields import PhoneNumberField


from vhmis_pro.utils import appointment_unique_slug_generator, report_unique_slug_generator
from accounts.models import UserAccount
from doctors.models import Doctor
from departments.models import Department


class Appointment(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)
    appointment_date = models.DateTimeField(auto_now=False, null=True)
    appointment_time = models.TimeField(auto_now=False, null=True)
    title = models.CharField(max_length=200)
    phone_number = PhoneNumberField(blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    message = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} - {self.title}'

    class Meta:
        ordering = ('-date_created',)


def appointment_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = appointment_unique_slug_generator(instance)


pre_save.connect(appointment_slug_generator, sender=Appointment)


class DiagnosticReport(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    remarks = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} - {self.title}'

    class Meta:
        ordering = ('-date_created',)


def report_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = report_unique_slug_generator(instance)


pre_save.connect(report_slug_generator, sender=DiagnosticReport)
