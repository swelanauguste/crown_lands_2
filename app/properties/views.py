from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.views.generic.edit import FormMixin

from .forms import PropertyCreateForm, PropertyUpdateForm, SurveyCreateForm
from .models import Property, Survey


class AddSurvey(FormMixin, DetailView):
    model = Property
    form_class = SurveyCreateForm

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


class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyCreateForm


class PropertyDetailView(DetailView):
    model = Property


class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyUpdateForm
    template_name_suffix = "_update_form"
