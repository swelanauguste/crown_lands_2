import os

from django.db import models
from django.urls import reverse
from locations.models import CommunityList, QuarterList
from mixins.assets import COMMUNITY_LIST, QUARTER_LIST, TimeStampMixin


class Property(TimeStampMixin):
    block = models.CharField(max_length=5, unique=True, null=True)
    parcel = models.CharField(max_length=3, unique=True, null=True)
    community = models.ForeignKey(
        CommunityList,
        related_name="property_communities",
        on_delete=models.CASCADE,
        null=True,
    )
    quarter = models.ForeignKey(
        QuarterList,
        related_name="property_quarters",
        on_delete=models.CASCADE,
        null=True,
    )
    quarter = models.CharField(max_length=50, null=True, choices=QUARTER_LIST)
    is_occupied = models.BooleanField(default=False, blank=True)
    is_acquired = models.BooleanField(default=False, blank=True)
    is_leased = models.BooleanField(default=False, blank=True)
    is_queen_chain = models.BooleanField("queen's chain", default=False, blank=True)
    is_available = models.BooleanField(default=False, blank=True)

    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "properties"
        unique_together = ["block", "parcel"]

    def get_update_url(self):
        return reverse("properties:property-update", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse("properties:property-detail", kwargs={"pk": self.pk})

    def get_object_full_address(self):
        return "%s, %s" % (self.community, self.quarter)

    def __str__(self):
        return "%s %s" % (self.block, self.parcel)


def survey_plans_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    new_filename = "%s_%s.%s" % (filename, instance.created, ext)
    return "survey_plans/{0}/{1}".format(instance.block_parcel, new_filename)


class Survey(TimeStampMixin):
    block_parcel = models.ForeignKey(
        Property, related_name="surveys", on_delete=models.SET_NULL, null=True
    )
    survey_plan_no = models.CharField(max_length=200, null=True)
    survey_plan = models.FileField(upload_to=survey_plans_directory_path, blank=True)
    date_surveyed = models.DateField(blank=True, null=True)
    parcel_h = models.PositiveIntegerField("hectares", default=0)
    parcel_f = models.PositiveIntegerField("feet", default=0)
    parcel_m = models.PositiveIntegerField("metres", default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return "%s" % (self.block_parcel)
