from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'orgs/$', OrgListView.as_view(), name='org-list'),
    re_path(r'^orgs/new/$', OrgCreateView.as_view(), name='org-new'),
    re_path(r'^orgs/delete/(?P<pk>\d+)$', OrgDeleteView.as_view(), name='org-delete'),
    re_path(r'^orgs/update/(?P<pk>\d+)$', OrgUpdateView.as_view(), name='org-update'),
]