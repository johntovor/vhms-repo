from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

from .choices import GENDER_CHOICES


class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, middle_name, last_name, gender, password=None, is_active=True, is_admin=False, is_staff=False, is_superuser=False, is_client=False):
        if not email:
            raise ValueError("Users must have an email address.")
        if not password:
            raise ValueError("Users must have a password.")
        if not first_name:
            raise ValueError("Users must have a first name.")
        if not last_name:
            raise ValueError("Users must have a last name.")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            gender=gender
        )

        user.set_password(password)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.is_superuser = is_superuser
        user.is_client = is_client
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, gender, middle_name=None, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            gender=gender,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, first_name, last_name, gender, middle_name=None, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            gender=gender,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True,
            is_client=True
        )
        return user


class UserAccount(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',
                              unique=True, max_length=255)
    first_name = models.CharField(max_length=255, verbose_name='Fisrt Name')
    middle_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=255, verbose_name='Last Name')
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    objects = UserAccountManager()

    def __str__(self):
        if self.middle_name:
            return f'{self.first_name} {self.middle_name} {self.last_name}'
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_first_name(self):
        return self.first_name


class SystemAdministrator(models.Model):
    """creates and saves a new pastor"""
    user = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        if self.user.middle_name:
            return f'{self.user.first_name} {self.user.middle_name} {self.user.last_name}'
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name_plural = 'System Administrators'


class Client(models.Model):
    """creates and saves a new member"""
    user = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, primary_key=True)
    region_or_state = models.CharField(max_length=250)
    city_or_town = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        if self.user.middle_name:
            return f'{self.user.first_name} {self.user.middle_name} {self.user.last_name}'
        return f'{self.user.first_name} {self.user.last_name}'
