from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django import forms

from .models import UserAccount, SystemAdministrator, Client
from .choices import GENDER_CHOICES


"""begin:: administrator creation form"""


class AdministratorForm(forms.ModelForm):

    """
    A form for creating new administrators. Includes all the required
    fields, plus a repeated password.
    """
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'First Name'
    }))
    middle_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Middle Name'
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Email'
    }))
    gender = forms.ChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control mb-4'
    }), choices=GENDER_CHOICES)
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={
                                'class': 'form-control mb-4',
                                'placeholder': 'Password'
                                }))
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput(attrs={
                                'class': 'form-control mb-4',
                                'placeholder': 'Repeat Password'
                                }))

    class Meta:
        model = UserAccount
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'gender')

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            UserAccount.objects.get(email__iexact=email)
            raise forms.ValidationError('Email already exists')
        except UserAccount.DoesNotExist:
            return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AdministratorForm, self).save(commit=False)
        user.is_admin = True
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        administrator = SystemAdministrator.objects.create(user=user)

        if commit:
            administrator.save()

        return user


"""end:: administrator creation form"""


"""begin:: cea client creation form"""


class ClientForm(forms.ModelForm):
    """
    A form for creating new clients. Includes all the required
    fields, plus a repeated password.
    """

    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'First Name'
    }))
    middle_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Middle Name'
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Email'
    }))
    region_or_state = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Region'
    }))
    city_or_town = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'City/Town'
    }))
    location = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Area where you live'
    }))
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='GH', attrs={
        'placeholder': 'Phone Number'
    }))
    gender = forms.ChoiceField(required=True, widget=forms.Select(attrs={
        'class': 'form-control mb-4'
    }), choices=GENDER_CHOICES)
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Repeat Password'
    }))

    class Meta:
        model = UserAccount
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'region_or_state', 'city_or_town', 'phone_number', 'location', 'gender')

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            UserAccount.objects.get(email__iexact=email)
            raise forms.ValidationError('Email already exists')
        except UserAccount.DoesNotExist:
            return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(ClientForm, self).save(commit=False)
        user.is_client = True
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        client = Client.objects.create(user=user)
        client.region_or_state = self.cleaned_data['region_or_state']
        client.city_or_town = self.cleaned_data['city_or_town']
        client.location = self.cleaned_data['location']
        client.phone_number = self.cleaned_data['phone_number']

        if commit:
            client.save()

        return user


"""end:: client creation form"""


"""begin:: user login form"""


class LoginForm(forms.Form):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Email'
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))


"""end:: user login form"""


"""begin:: profile updates form"""


class UserUpdateForm(forms.ModelForm):
    """updates user email"""
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Enter new email here...'
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4'
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Enter your phone number here...'
    }))
    # profile_pic = forms.ImageField(widget=forms.FileInput(attrs={
    #     'class': 'form-control mb-4'
    # }))

    class Meta():
        model = UserAccount
        fields = ('email', 'location', 'phone_number')


"""end:: profile update"""


"""begin:: client profile update form"""


class ClientProfileUpdateForm(forms.ModelForm):

    """updates other fields of client profile"""
    # fellowship = forms.ModelChoiceField(queryset=fellowships, required=True, widget=forms.Select(attrs={
    #     'class': 'form-control mb-4',
    #     'placeholder': 'Select fellowship...'
    # }))
    # cell = forms.ModelChoiceField(queryset=cells, required=True, widget=forms.Select(attrs={
    #     'class': 'form-control mb-4',
    #     'placeholder': 'Select fellowship...'
    # }))
    # department = forms.ModelChoiceField(queryset=departments, required=False, widget=forms.Select(attrs={
    #     'class': 'form-control mb-4',
    #     'placeholder': 'Select fellowship...'
    # }))
    pass

    # class Meta():
    #     model = client
    #     fields = ('cell', 'fellowship', 'department')


"""end:: client profile update form"""


"""begin:: user admin creation form"""


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


"""end:: user admin creation form"""


"""begin:: user admin change form"""


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserAccount
        fields = ('email', 'password', 'is_active',
                  'is_admin', 'is_staff', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


"""end:: user admin change form"""
