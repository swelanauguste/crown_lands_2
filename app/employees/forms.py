from django import forms
from .models import Employee


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = [
            "updated_by",
            "created_by",
            "employee",
            "employment_id",
            "position",
            "grade",
            "is_commissioner",
            "is_deputy_commissioner",
        ]
