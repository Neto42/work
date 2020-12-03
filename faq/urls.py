from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^quests/$', QuestionListView.as_view(), name='quest-list'),
]