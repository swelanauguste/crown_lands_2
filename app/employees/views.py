from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView

from .models import Employee
from .forms import EmployeeUpdateForm


class EmployeeListView(ListView):
    model = Employee


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeUpdateForm
    template_name_suffix = "_update_form"


class EmployeeDetailView(DetailView):
    model = Employee
