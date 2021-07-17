from django import forms
from .models import Property, Survey


class SurveyCreateForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            # "block_parcel": forms.HiddenInput(),
            "notes": forms.Textarea(attrs={"rows": 3}),
            "date_surveyed": forms.DateInput(attrs={"type": "date"}),
        }


class PropertyCreateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {"notes": forms.Textarea(attrs={"rows": 3})}


class PropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {"notes": forms.Textarea(attrs={"rows": 3})}
