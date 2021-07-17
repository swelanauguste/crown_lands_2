from django import forms
from django.forms import widgets
from mixins.assets import LAND_USE_LIST, EASEMENT_LIST, APPLICATION_TYPE

from .models import IndividualApplication


class IndividualApplicationCreateForm(forms.ModelForm):
    class Meta:
        model = IndividualApplication
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
            "application_type": forms.CheckboxSelectMultiple(),
            "land_use": forms.CheckboxSelectMultiple(),
            "easement": forms.CheckboxSelectMultiple(),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }


class IndividualApplicationUpdateForm(forms.ModelForm):
    class Meta:
        model = IndividualApplication
        fields = "__all__"
        exclude = [
            "created_by",
            "updated_by",
            "date_received",
            "application_number",
            "status",
            "received_at",
        ]
        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
            "application_type": forms.CheckboxSelectMultiple(),
            "land_use": forms.CheckboxSelectMultiple(),
            "easement": forms.CheckboxSelectMultiple(),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }
