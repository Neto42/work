from django.views.generic import TemplateView, ListView

from hh_site.models import Work, Ad
from organization.models import Organization
from comment.models import CommentAd, CommentAnswer, CommentOrganization, CommentQuestion


class HomePageView(TemplateView):
    template_name = "html/hh_site/fwork.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work'] = Work.objects.all().count()
        context['ad'] = Ad.objects.all().count()
        context['organization'] = Organization.objects.all().count()
        context['comments'] = (CommentAd.objects.all().count() + CommentOrganization.objects.all().count()
                               + CommentQuestion.objects.all().count() + CommentAnswer.objects.all().count())

        return context


class AdListView(ListView):
    model = Work
    template_name = "html/hh_site/ad_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = Ad.objects.all()

        return context
