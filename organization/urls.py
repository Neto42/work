from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^org/new/$', OrgCreateView.as_view(), name='org-new'),
]