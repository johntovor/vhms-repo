from django import forms

from .models import Department


class DepartmentForm(forms.ModelForm):
    
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Department Name'
    }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Department Description'
    }))

    class Meta:
        model = Department
        exclude = ['date_created', 'slug']
