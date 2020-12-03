from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

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
