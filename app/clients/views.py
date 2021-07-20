from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import FormMixin

from .forms import (
    IdentificationCreateForm,
    IdentificationUpdateForm,
    IndividualCreateForm,
    IndividualUpdateForm,
)
from .models import Identification, Individual


class IdentificationList(LoginRequiredMixin, ListView):
    model = Identification


class IdentificationDetail(LoginRequiredMixin, DetailView):
    model = Identification


class IdentificationUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Identification
    form_class = IdentificationUpdateForm
    template_name_suffix = "_update_form"
    success_message = "%(individual)s was updated successfully"


class AddIdentification(LoginRequiredMixin, SuccessMessageMixin, FormMixin, DetailView):
    model = Individual
    form_class = IdentificationCreateForm
    template_name_suffix = "_create_form"
    success_message = "%(individual)s was updated successfully"

    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()

    def get_initial(self):
        return {"individual": self.get_object()}

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IdentificationCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Identification
    form_class = IdentificationCreateForm


class IndividualList(LoginRequiredMixin, ListView):
    model = Individual


class IndividualDetail(LoginRequiredMixin, DetailView):
    model = Individual


class IndividualUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Individual
    form_class = IndividualUpdateForm
    template_name_suffix = "_update_form"
    success_message = "%(title)s %(first_name)s %(last_name)s was updated successfully"


class IndividualCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Individual
    form_class = IndividualCreateForm
    success_message = "%(title)s %(first_name)s %(last_name)s was created successfully"
