from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseForbidden
from .models import IndividualApplication
from .forms import IndividualApplicationCreateForm, IndividualApplicationUpdateForm, AssignApplicationForm



class AssignApplicationDetailFormView(FormMixin, DetailView):
    model = IndividualApplication
    form_class = AssignApplicationForm

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
    form_class = IndividualApplicationUpdateForm
    template_name_suffix = '_update_form'
