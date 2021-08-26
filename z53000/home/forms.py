import django.forms
from django.forms import ModelForm
from .models import News


class NewNew(ModelForm):

    class Meta:
        model = News
        fields = ('title', 'content', 'category')