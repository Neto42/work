from django.forms import ModelForm

from faq.models import Question, Answer


class QuestForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class AnsForm(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
