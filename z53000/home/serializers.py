from rest_framework import serializers

from .models import News


class NewsJson(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'content', 'published')
