from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from .models import Individual, Identification
from .forms import IndividualCreateForm, IndividualUpdateForm


class IdentificationList(ListView):
    model = Identification


class IdentificationDetail(DetailView):
    model = Identification


class IdentificationUpdate(UpdateView):
    model = Identification
    fields = "__all__"
    template_name_suffix = "_update_form"


class IdentificationCreate(CreateView):
    model = Identification
    fields = "__all__"


class IndividualList(ListView):
    model = Individual


class IndividualDetail(DetailView):
    model = Individual


class IndividualUpdate(UpdateView):
    model = Individual
    form_class = IndividualCreateForm
    template_name_suffix = "_update_form"


class IndividualCreate(CreateView):
    model = Individual
    form_class = IndividualUpdateForm
