from django.forms import ModelForm

from hh_site.models import Ad, Work


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ('work', 'organization', 'ad_text', 'salary')


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ('work',)
