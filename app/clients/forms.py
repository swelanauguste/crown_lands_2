from django import forms

from .models import Individual, Identification


class IndividualCreateForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = "__all__"
        exclude = ["created_by", "updated_by", 'deceased']
        widgets = {"title": forms.Select(attrs={"type": "radio"})}


class IndividualUpdateForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
