from django import forms

from .models import Doctor
from departments.models import Department


departments = Department.objects.all()


class DoctorForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Provide name of doctor'
    }))

    department = forms.ModelChoiceField(queryset=departments, required=True, widget=forms.Select(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Select department'
    }))



    class Meta:
        model = Doctor
        exclude = ['date_added', 'slug']
