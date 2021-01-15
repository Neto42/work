from django.forms import ModelForm

from organization.models import Organization


class OrgForm(ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'
