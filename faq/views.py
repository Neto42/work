from django.shortcuts import render
from django.views.generic import ListView

from faq.models import Question, Answer


class QuestionListView(ListView):
    model = Question
    template_name = "html/faq/quest_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.order_by('theme', 'id')[:self.paginate_by]
