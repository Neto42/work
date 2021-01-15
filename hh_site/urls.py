from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('^$', HomePageView.as_view(), name='fwork'),
    re_path('^we', WePageView.as_view(), name='my'),
    re_path(r'^ads/$', AdListView.as_view(), name='ad-list'),
    re_path(r'^ads/ad-(?P<pk>\d+)$', AdDetailView.as_view(), name='ad-detail'),
    re_path(r'^ad/new/$', AdCreateView.as_view(), name='ad-new'),
    re_path(r'^ad/update/(?P<pk>\d+)$', AdUpdateView.as_view(), name='ad-update'),
    re_path(r'^ad/delete/(?P<pk>\d+)$', AdDeleteView.as_view(), name='ad-delete'),
    re_path(r'works$', WorkListView.as_view(), name='work-list'),
    re_path(r'works/new/$', WorkCreateView.as_view(), name='work-new'),
]