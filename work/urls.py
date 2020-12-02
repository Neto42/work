from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/fwork/', permanent=True)),
    path('fwork/', include('hh_site.urls')),
    # path('organization/', include('organization.urls')),
]
