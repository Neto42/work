from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from organization.forms import OrgForm


class OrgCreateView(CreateView):
    form_class = OrgForm
    template_name = 'html/hh_site/org-new.html'
    success_url = reverse_lazy('fwork')
