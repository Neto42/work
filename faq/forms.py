from django.forms import ModelForm

from faq.models import Question, Answer


class QuestForm(ModelForm):
    class Meta:
        model = Question
        fields = ('theme', 'text')


class AnsForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('quest', 'theme', 'text')
