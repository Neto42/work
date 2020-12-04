from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from hh_site.forms import AdForm
from hh_site.models import Work, Ad
from organization.models import Organization
from comment.models import CommentAnswer, CommentQuestion


class HomePageView(TemplateView):
    template_name = "html/hh_site/fwork.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work'] = Work.objects.all().count()
        context['ad'] = Ad.objects.all().count()
        context['organization'] = Organization.objects.all().count()
        context['comments'] = (CommentQuestion.objects.all().count() + CommentAnswer.objects.all().count())

        return context


class AdListView(ListView):
    model = Ad
    template_name = "html/hh_site/ad_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Ad.objects.order_by('work', 'organization')[:self.paginate_by]


class AdDetailView(DetailView):
    model = Ad
    template_name = "html/hh_site/ad_detail.html"


class AdCreateView(CreateView):
    form_class = AdForm
    template_name = 'html/hh_site/ad_new.html'
    success_url = reverse_lazy('ad-list')


class AdUpdateView(UpdateView):
    model = Ad
    form_class = AdForm
    template_name = 'html/hh_site/ad_update.html'
    success_url = reverse_lazy('ad-list')


class AdDeleteView(DeleteView):
    model = Ad
    form_class = AdForm
    template_name = 'html/hh_site/ad_delete.html'
    success_url = reverse_lazy('ad-list')
