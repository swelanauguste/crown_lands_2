from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Property, Survey


class PropertyListView(ListView):
    model = Property


class PropertyCreateView(CreateView):
    model = Property
    fields = "__all__"


class PropertyDetailView(DetailView):
    model = Property


class PropertyUpdateView(UpdateView):
    model = Property
    fields = "__all__"
    template_name_suffix = "_update_form"
