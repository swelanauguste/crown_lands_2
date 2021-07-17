from django.db import models
from mixins.assets import TimeStampMixin

# Create your models here.
class CommunityList(TimeStampMixin):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class QuarterList(TimeStampMixin):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
