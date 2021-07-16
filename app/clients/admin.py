from django.contrib import admin

from .models import Identification, Individual

admin.site.register(Individual)
admin.site.register(Identification)