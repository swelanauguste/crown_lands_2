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


class ApplicationStatus(TimeStampMixin):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Application Statuses"

    def __str__(self):
        return self.name


class LandUse(TimeStampMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ApplicationType(TimeStampMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Easement(TimeStampMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class IndividualApplication(TimeStampMixin):
    status = models.ForeignKey(
        ApplicationStatus,
        related_name="application_statuses",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    applicant = models.ManyToManyField(Individual)
    block_parcel = models.ForeignKey(Property, null=True, on_delete=models.SET_NULL)
    filing_number = models.CharField(max_length=200, unique=True, null=True, blank=True)
    application_number = models.CharField(
        max_length=20, unique=True, null=True, blank=True
    )
    date_received = models.DateField(null=True, blank=True)
    application_type = models.ManyToManyField(ApplicationType)
    received_at = models.CharField(
        max_length=255, default="CASTRIES", choices=OFFICE_LIST
    )
    # is_queen_chain = models.BooleanField("queen's chain", default=False, blank=True)
    occupied_by_me = models.BooleanField(default=False, blank=True)
    years_occupied_by_me = models.PositiveSmallIntegerField(null=True, blank=True)
    area_requested = models.CharField(
        max_length=10, null=True, blank=True, help_text="(imperial/metric)"
    )
    land_use = models.ManyToManyField(LandUse)
    other_land_uses = models.CharField(max_length=200, blank=True, null=True)
    # response_date = models.DateTimeField(blank=True, null=True)
    easement = models.ManyToManyField(Easement)
    other_easement = models.CharField(max_length=200, blank=True, null=True)
    # date_completed = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    application_form = models.FileField(
        upload_to=application_documents_directory_path, blank=True
    )

    def get_update_url(self):
        return reverse("applications:individual-update", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse("applications:individual-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return "%s | %s" % (self.block_parcel, self.application_number)


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
