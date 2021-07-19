from django.db import models
from django.db.models.enums import Choices

from mixins.assets import TimeStampMixin, POSITION_LIST, GRADE_LIST
from django.urls import reverse

from django.conf import settings

Employee = settings.AUTH_USER_MODEL


class Position(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Grade(TimeStampMixin):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True)
    employment_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=25, null=True, blank=True)
    position = models.ForeignKey(
        Position,
        related_name="employee_positions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    grade = models.ForeignKey(
        Grade,
        related_name="employee_grades",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_commissioner = models.BooleanField(default=False)
    is_deputy_commissioner = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("employees:employee-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("employees:employee-update", kwargs={"pk": self.pk})

    def get_full_name(self):
        if self.first_name and self.last_name:
            return "%s, %s" % (self.last_name, self.first_name)
        return self.employee

    def get_employee_email(self):
        return self.employee.email

    def __str__(self):
        if self.first_name and self.last_name:
            return "%s, %s" % (self.last_name, self.first_name)
        return str(self.employee)
