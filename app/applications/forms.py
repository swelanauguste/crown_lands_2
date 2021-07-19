from django import forms
from .models import IndividualApplication, AssignApplication
from employees.models import Employee


class AssignApplicationForm(forms.ModelForm):
    class Meta:
        model = AssignApplication
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "application": forms.HiddenInput(),
        }
    
    def __init__(self, user=None, **kwargs):
        super(AssignApplicationForm, self).__init__(**kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(position=1)


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
