from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


from .models import Appointment, DiagnosticReport
from accounts.models import UserAccount
from departments.models import Department
from doctors.models import Doctor


users = UserAccount.objects.filter(is_client=True, is_superuser=False).all()
departments = Department.objects.all()
doctors = Doctor.objects.all()


class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateTimeField(required=True, label="Date", widget=forms.DateTimeInput(attrs={
        "type": "date",
        'class': 'form-control mb-4',
        'placeholder': 'Appointment Date'
    }))
    appointment_time = forms.TimeField(required=True, label="Time", widget=forms.DateTimeInput(attrs={
        "type": "time",
        'class': 'form-control mb-4',
        'placeholder': 'Appointment Time'
    }))
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='GH', attrs={
        'placeholder': 'Phone Number'
    }))
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Title: Eg, Appointment for my dog'
    }))
    department = forms.ModelChoiceField(queryset=departments, required=True, widget=forms.Select(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Select department'
    }))
    doctor = forms.ModelChoiceField(queryset=doctors, required=True, widget=forms.Select(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Select doctor'
    }))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'This field is option. You can add any extra information you want to pass across.'
    }))
    

    class Meta:
        model = Appointment
        exclude = ['user', 'date_created', 'slug']


class DiagnosticReportForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=users, required=True, widget=forms.Select(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Select doctor'
    }))
    doctor = forms.ModelChoiceField(queryset=doctors, required=True, widget=forms.Select(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Select doctor'
    }))
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Title: Eg, Appointment for my dog'
    }))
    remarks = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Add doctor\'s diagnostic remarks here.'
    }))
    

    class Meta:
        model = DiagnosticReport
        exclude = ['date_created', 'slug']
