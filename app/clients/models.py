from django.db import models
from django.urls import reverse
from mixins.assets import (
    TimeStampMixin,
    NATIONALITY_LIST,
    TYPE_OF_IDENTIFICATION_LIST,
    TITLE_LIST,
    COMMUNITY_LIST,
    QUARTER_LIST,
)
from locations.models import CommunityList, QuarterList


class Individual(TimeStampMixin):
    title = models.CharField(max_length=50, choices=TITLE_LIST)
    last_name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    middle_name = models.CharField(max_length=200, blank=True)
    alias = models.CharField(max_length=20, blank=True)
    occupation = models.CharField(max_length=200, blank=True)
    postal_address = models.CharField(
        max_length=200,
        blank=True,
        help_text="<small>eg.: c/o Conway Post Office, Waterfront, Castries</small>",
    )
    community = models.ForeignKey(
        CommunityList,
        related_name="individual_communities",
        on_delete=models.SET_NULL,
        null=True,
    )
    quarter = models.ForeignKey(
        QuarterList,
        related_name="individual_quarters",
        on_delete=models.SET_NULL,
        null=True,
    )
    home_address = models.CharField(
        max_length=200,
        blank=True,
        help_text="<small>Please an address if it is not listed above</small>",
    )
    tel1 = models.CharField(max_length=25, blank=True)
    tel2 = models.CharField(max_length=25, blank=True)
    email = models.EmailField(blank=True)
    nationality = models.CharField(
        max_length=40, choices=NATIONALITY_LIST, default="Saint Lucian"
    )
    deceased = models.BooleanField(default=False)

    class Meta:
        ordering = ["last_name"]

    def get_update_url(self):
        return reverse("clients:individual-update", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse("clients:individual-detail", kwargs={"pk": self.pk})

    def get_object_full_name(self):
        if self.middle_name and self.first_name and self.last_name:
            return "%s, %s %s" % (self.last_name, self.first_name, self.middle_name)
        return "%s, %s" % (self.last_name, self.first_name)

    def get_object_full_address(self):
        if self.home_address:
            return self.home_address
        return "%s, %s" % (self.community, self.quarter)

    def __str__(self):
        if self.middle_name and self.first_name and self.last_name:
            return "%s, %s %s" % (self.last_name, self.first_name, self.middle_name)
        return "%s, %s" % (self.last_name, self.first_name)


def identification_documents_directory_path(instance, filename):
    return "individual_identification_documents/{0}/{1}/{2}".format(
        instance.id_type, instance.individual.id, filename
    )


class Identification(TimeStampMixin):
    id_type = models.CharField(
        "Type", max_length=50, choices=TYPE_OF_IDENTIFICATION_LIST
    )
    individual = models.ForeignKey(
        Individual, related_name="identifications", null=True, on_delete=models.SET_NULL
    )
    file = models.FileField(upload_to=identification_documents_directory_path)

    def __str__(self):
        return str(self.file)
