from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView

from .models import Employee


class EmployeeListView(ListView):
    model = Employee


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = "__all__"


class EmployeeDetailView(DetailView):
    model = Employee
