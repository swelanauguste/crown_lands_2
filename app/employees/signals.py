from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import Employee

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.get_or_create(employee=instance)


@receiver(post_save, sender=User)
def save_employee_profile(sender, instance, **kwargs):
    instance.employee.save()