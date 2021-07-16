from django.contrib import admin

from .models import (
    IndividualApplication,
    AssignApplication,
)


@admin.register(AssignApplication)
class AssignApplicationAdmin(admin.ModelAdmin):
    list_display = ["pk", "application", "employee"]
    list_editable = ["employee"]


@admin.register(IndividualApplication)
class IndividualApplicationAdmin(admin.ModelAdmin):
    list_display = ["applicant_number", "status", "pk"]
    list_editable = ["status"]
