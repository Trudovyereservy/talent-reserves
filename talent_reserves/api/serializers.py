from rest_framework import serializers
from news.models import News, ContentNews


class ContentNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentNews
        fields = ['id', 'image']


class NewsSerializer(serializers.ModelSerializer):
    related_content = ContentNewsSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'content',
                  'date_published', 'images']
