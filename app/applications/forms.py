from django import forms
from django.forms import widgets

from .models import IndividualApplication


class IndividualApplicationCreateForm(forms.ModelForm):
    class Meta:
        model = IndividualApplication
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
            "land_use": forms.CheckboxSelectMultiple(),
            "easement": forms.CheckboxSelectMultiple(),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }
