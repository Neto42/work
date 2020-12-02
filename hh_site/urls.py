from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('^$', HomePageView.as_view(), name='fwork'),
    re_path('^ad', AdListView.as_view(), name='ad-list'),
]