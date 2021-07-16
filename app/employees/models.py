from django.db import models
from django.db.models.enums import Choices

from mixins.assets import TimeStampMixin, POSITION_LIST, GRADE_LIST
from django.urls import reverse

from django.conf import settings

Employee = settings.AUTH_USER_MODEL


class Employee(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True)
    employment_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=25, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True, choices=POSITION_LIST)
    grade = models.CharField(max_length=200, null=True, blank=True, choices=GRADE_LIST)
    is_commissioner = models.BooleanField(default=False)
    is_deputy_commissioner = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("employees:detail", kwargs={"pk": self.pk})

    def get_full_name(self):
        if self.first_name and self.last_name:
            return "%s, %s" % (self.last_name, self.first_name)
        return self.employee.username

    def __str__(self):
        return str(self.employee.username)
