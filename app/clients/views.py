from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseForbidden

from .forms import (
    IdentificationCreateForm,
    IdentificationUpdateForm,
    IndividualCreateForm,
    IndividualUpdateForm,
)
from .models import Identification, Individual


class IdentificationList(ListView):
    model = Identification


class IdentificationDetail(DetailView):
    model = Identification


class IdentificationUpdate(UpdateView):
    model = Identification
    form_class = IdentificationUpdateForm
    template_name_suffix = "_update_form"


class AddIdentification(FormMixin, DetailView):
    model = Individual
    form_class = IdentificationCreateForm
    template_name_suffix = "_create_form"

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


class IdentificationCreate(CreateView):
    model = Identification
    form_class = IdentificationCreateForm


class IndividualList(ListView):
    model = Individual


class IndividualDetail(DetailView):
    model = Individual


class IndividualUpdate(UpdateView):
    model = Individual
    form_class = IndividualUpdateForm
    template_name_suffix = "_update_form"


class IndividualCreate(CreateView):
    model = Individual
    form_class = IndividualCreateForm
