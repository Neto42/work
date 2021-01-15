from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from comment.models import CommentAnswer, CommentQuestion
from hh_site.forms import AdForm, WorkForm
from hh_site.models import Work, Ad
from organization.models import Organization
from user.models import Profile


class HomePageView(TemplateView):
    template_name = "html/hh_site/fwork.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work'] = Work.objects.all().count()
        context['ad'] = Ad.objects.all().count()
        context['organization'] = Organization.objects.all().count()
        context['comments'] = (CommentQuestion.objects.all().count() + CommentAnswer.objects.all().count())

        return context


class WePageView(TemplateView):
    template_name = "html/my/my.html"


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

    def form_valid(self, form):
        form.instance.user = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


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


class WorkCreateView(CreateView):
    form_class = WorkForm
    template_name = 'html/hh_site/work-new.html'
    success_url = reverse_lazy('work-list')


class WorkListView(ListView):
    model = Work
    template_name = "html/hh_site/work_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Work.objects.order_by('work',)[:self.paginate_by]


class WorkUpdateView(UpdateView):
    model = Work
    form_class = WorkForm
    template_name = 'html/hh_site/work_update.html'
    success_url = reverse_lazy('work-list')


class WorkDeleteView(DeleteView):
    model = Work
    form_class = WorkForm
    template_name = 'html/hh_site/work_delete.html'
    success_url = reverse_lazy('work-list')
