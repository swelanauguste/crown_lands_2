from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.edit import FormMixin

from .forms import PropertyCreateForm, PropertyUpdateForm, SurveyCreateForm
from .models import Property, Survey


class AddSurvey(LoginRequiredMixin, SuccessMessageMixin, FormMixin, DetailView):
    model = Property
    form_class = SurveyCreateForm
    success_message = "%(block_parcel)s was added successfully"

    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()

    def get_initial(self):
        return {"block_parcel": self.get_object()}

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


class PropertyListView(ListView):
    model = Property


class PropertyCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Property
    form_class = PropertyCreateForm
    success_message = "%(block)s  %(parcel)s was created successfully"


class PropertyDetailView(LoginRequiredMixin, DetailView):
    model = Property


class PropertyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Property
    form_class = PropertyUpdateForm
    template_name_suffix = "_update_form"
    success_message = "%(block)s  %(parcel)s was updated successfully"
