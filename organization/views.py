from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from organization.forms import OrgForm
from organization.models import Organization


class OrgCreateView(CreateView):
    form_class = OrgForm
    template_name = 'html/hh_site/org-new.html'
    success_url = reverse_lazy('org-list')


class OrgDeleteView(DeleteView):
    form_class = OrgForm
    model = Organization
    template_name = 'html/hh_site/org-delete.html'
    success_url = reverse_lazy('org-list')


class OrgUpdateView(UpdateView):
    form_class = OrgForm
    model = Organization
    template_name = 'html/hh_site/org_update.html'
    success_url = reverse_lazy('org-list')


class OrgListView(ListView):
    model = Organization
    template_name = "html/hh_site/org_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Organization.objects.order_by('organization')
