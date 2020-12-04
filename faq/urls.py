from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^quests/$', QuestionListView.as_view(), name='quest-list'),
    re_path(r'^quest/new/$', QuestCreateView.as_view(), name='quest-new'),
    re_path(r'^answer/new/$', AnswerCreateView.as_view(), name='ans-new'),
    re_path(r'^quest/delete/(?P<pk>\d+)$', QuestDeleteView.as_view(), name='quest-delete'),
    re_path(r'^answer/delete/(?P<pk>\d+)$', AnswerDeleteView.as_view(), name='answer-delete'),
]