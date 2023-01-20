from django.db import models
from django.db.models.signals import pre_save

# from vhmis_pro.utils import doctor_unique_slug_generator
# from accounts.models import UserAccount
# from business.models import Business
# from .choices import PAYMENT_STATUS_CHOICES, PAYMENT_METHOD_CHOICES


# class Payment(models.Model):
#     user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)
#     business_name = models.ForeignKey(
#         Business, on_delete=models.CASCADE, null=True)
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
#     receipt_id = models.CharField(max_length=250)
#     payer = models.CharField(max_length=250)
#     payment_method = models.CharField(
#         max_length=200, choices=PAYMENT_METHOD_CHOICES)
#     payment_status = models.CharField(
#         max_length=100, choices=PAYMENT_STATUS_CHOICES)
#     payment_date = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField(max_length=300, null=True, blank=True)

#     def __str__(self):
#         if self.user.middle_name:
#             return f'{self.user.first_name} {self.user.middle_name} {self.user.last_name}'
#         return f'{self.user.first_name} {self.user.last_name}'

#     class Meta:
#         ordering = ('-payment_date',)


# def payment_slug_generator(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = payment_unique_slug_generator(instance)


# pre_save.connect(payment_slug_generator, sender=Payment)
