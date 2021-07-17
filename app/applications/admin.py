from django.contrib import admin

from .models import (
    IndividualApplication,
    AssignApplication,
    ApplicationStatus,
    ApplicationType,
    Easement,
    LandUse
)

admin.site.register(ApplicationStatus)
admin.site.register(ApplicationType)
admin.site.register(Easement)
admin.site.register(LandUse)


@admin.register(AssignApplication)
class AssignApplicationAdmin(admin.ModelAdmin):
    list_display = ["pk", "application", "employee"]
    list_editable = ["employee"]


@admin.register(IndividualApplication)
class IndividualApplicationAdmin(admin.ModelAdmin):
    list_display = ["application_number", "status", "pk"]
    list_editable = ["status"]
