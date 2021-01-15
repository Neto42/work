from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from organization.forms import OrgForm
from organization.models import Organization


class OrgCreateView(CreateView):
    form_class = OrgForm
    template_name = 'html/hh_site/org-new.html'
    success_url = reverse_lazy('org-list')


class OrgListView(ListView):
    model = Organization
    template_name = "html/hh_site/org_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Organization.objects.order_by('organization')[:self.paginate_by]