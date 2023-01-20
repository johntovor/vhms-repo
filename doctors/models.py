from django.db import models
from django.db.models.signals import pre_save

from vhmis_pro.utils import doctor_unique_slug_generator
from departments.models import Department

class Doctor(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('-date_added',)
        


def doctor_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = doctor_unique_slug_generator(instance)


pre_save.connect(doctor_slug_generator, sender=Doctor)
