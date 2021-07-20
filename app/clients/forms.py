from django import forms

from .models import Individual, Identification


class IdentificationCreateForm(forms.ModelForm):
    class Meta:
        model = Identification
        fields = ["individual", "id_type", "id_number", "file"]
        widgets = {
            "individual": forms.HiddenInput(),
        }


class IdentificationUpdateForm(forms.ModelForm):
    class Meta:
        model = Identification
        fields = ["individual", "id_type", "file"]


class IndividualCreateForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = "__all__"
        exclude = ["created_by", "updated_by", "deceased"]
        widgets = {"title": forms.Select(attrs={"type": "radio"})}


class IndividualUpdateForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
