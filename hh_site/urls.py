from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('^$', HomePageView.as_view(), name='fwork'),
]