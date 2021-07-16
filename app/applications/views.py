from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .models import IndividualApplication
from .forms import IndividualApplicationCreateForm


class Index(TemplateView):
    template_name = 'index.html'

class IndividualApplicationList(ListView):
    model = IndividualApplication


class IndividualApplicationDetail(DetailView):
    model = IndividualApplication


class IndividualApplicationCreate(CreateView):
    model = IndividualApplication
    form_class = IndividualApplicationCreateForm


class IndividualApplicationUpdate(UpdateView):
    model = IndividualApplication
    fields = "__all__"
