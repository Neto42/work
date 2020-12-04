from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from faq.forms import QuestForm, AnsForm
from faq.models import Question, Answer


class QuestionListView(ListView):
    model = Question
    template_name = "html/faq/quest_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.order_by('theme', 'id')[:self.paginate_by]


class QuestCreateView(CreateView):
    form_class = QuestForm
    template_name = 'html/faq/quest_new.html'
    success_url = reverse_lazy('quest-list')


# class AdUpdateView(UpdateView):
#     model = Ad
#     form_class = AdForm
#     template_name = 'html/hh_site/ad_update.html'
#     success_url = reverse_lazy('ad-list')


class QuestDeleteView(DeleteView):
    model = Question
    form_class = QuestForm
    template_name = 'html/faq/quest_delete.html'
    success_url = reverse_lazy('quest-list')


class AnswerCreateView(CreateView):
    form_class = AnsForm
    template_name = 'html/faq/ans_new.html'
    success_url = reverse_lazy('quest-list')


class AnswerDeleteView(DeleteView):
    model = Answer
    form_class = AnsForm
    template_name = 'html/faq/ans_delete.html'
    success_url = reverse_lazy('quest-list')
