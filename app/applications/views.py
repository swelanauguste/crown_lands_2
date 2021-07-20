from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from django.views.generic.edit import FormMixin

from .forms import (
    AssignApplicationForm,
    IndividualApplicationCreateForm,
    IndividualApplicationUpdateForm,
)
from .models import IndividualApplication


class AssignApplicationDetailFormView(
    LoginRequiredMixin, SuccessMessageMixin, FormMixin, DetailView
):
    model = IndividualApplication
    form_class = AssignApplicationForm
    success_message = (
        "Application %(application)s was assigned to %(employee)s successfully"
    )

    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()

    def get_initial(self):
        return {"application": self.get_object()}

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


class Index(TemplateView):
    template_name = "index.html"


class IndividualApplicationList(LoginRequiredMixin, ListView):
    model = IndividualApplication


class IndividualApplicationDetail(LoginRequiredMixin, DetailView):
    model = IndividualApplication


class IndividualApplicationCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = IndividualApplication
    form_class = IndividualApplicationCreateForm
    success_message = "Application %(application_number)s was created to successfully"


class IndividualApplicationUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = IndividualApplication
    form_class = IndividualApplicationUpdateForm
    template_name_suffix = "_update_form"
    success_message = "Application %(block_parcel)s was updated to successfully"
