from django.db import models
from django.db.models.signals import pre_save

from vhmis_pro.utils import department_unique_slug_generator
from accounts.models import UserAccount




class Department(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=560, null=True, blank=True)

    def __str__(self):
        if self.name:
            return f'{self.name}'

    class Meta:
        ordering = ('-date_created',)


def department_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = department_unique_slug_generator(instance)


pre_save.connect(department_slug_generator, sender=Department)
