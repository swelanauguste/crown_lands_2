from django.db import models
from django.urls import reverse
from mixins.assets import (
    TimeStampMixin,
    OFFICE_LIST,
    APPLICATION_STATUS_LIST,
    APPLICATION_TYPE,
    LAND_USE_LIST,
    EASEMENT_LIST,
)
from properties.models import Property
from employees.models import Employee
from clients.models import Individual


def application_documents_directory_path(instance, filename):
    return "application_documents/{0}/{1}".format(instance.id, filename)


class IndividualApplication(TimeStampMixin):
    filing_number = models.CharField(max_length=200, unique=True, blank=True)
    applicant_number = models.CharField(
        max_length=20, unique=True, null=True, blank=True
    )
    date_received = models.DateField(null=True, blank=True)
    applicant = models.ForeignKey(
        Individual, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(
        max_length=20, default="pending", choices=APPLICATION_STATUS_LIST
    )
    block_parcel = models.ForeignKey(Property, null=True, on_delete=models.SET_NULL)
    application_type = models.CharField(
        max_length=20, default="PURCHASE", choices=APPLICATION_TYPE
    )
    received_at = models.CharField(
        max_length=20, default="CASTRIES", choices=OFFICE_LIST
    )
    land_use = models.CharField(
        max_length=20, default="RESIDENTIAL", choices=LAND_USE_LIST
    )
    other_land_uses = models.CharField(max_length=200, blank=True, null=True)
    response_date = models.DateTimeField(blank=True, null=True)
    easement = models.CharField(
        max_length=25, default="WATER CONNECTION", choices=EASEMENT_LIST
    )
    other_easement = models.CharField(max_length=200, blank=True, null=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    file = models.FileField(upload_to=application_documents_directory_path, blank=True)

    def get_absolute_url(self):
        return reverse("applications:individual-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return "%s | %s" % (self.block_parcel, self.applicant)


class AssignApplication(TimeStampMixin):
    application = models.ForeignKey(
        IndividualApplication,
        related_name="assign_applications",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return "application %s is assigned to %s" % (self.application, self.employee)