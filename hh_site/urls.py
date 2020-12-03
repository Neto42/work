from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('^$', HomePageView.as_view(), name='fwork'),
    re_path(r'^ads/$', AdListView.as_view(), name='ad-list'),
    re_path(r'^ads/ad-(?P<pk>\d+)$', AdDetailView.as_view(), name='ad-detail'),
]