from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from faq.forms import QuestForm, AnsForm
from faq.models import Question, Answer
from user.models import Profile


class QuestionListView(ListView):
    model = Question
    template_name = "html/faq/quest_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Question.objects.order_by('theme', 'id')


class QuestCreateView(CreateView):
    model = Question
    form_class = QuestForm
    template_name = 'html/faq/quest_new.html'
    success_url = reverse_lazy('quest-list')

    def form_valid(self, form):
        form.instance.user = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


class QuestDeleteView(DeleteView):
    model = Question
    form_class = QuestForm
    template_name = 'html/faq/quest_delete.html'
    success_url = reverse_lazy('quest-list')


class AnswerCreateView(CreateView):
    form_class = AnsForm
    model = Answer
    template_name = 'html/faq/ans_new.html'
    success_url = reverse_lazy('quest-list')

    def form_valid(self, form):
        form.instance.user = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


class AnswerDeleteView(DeleteView):
    model = Answer
    form_class = AnsForm
    template_name = 'html/faq/ans_delete.html'
    success_url = reverse_lazy('quest-list')
