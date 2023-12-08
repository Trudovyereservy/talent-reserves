from rest_framework import serializers

from coaches.models import Coach
from news.models import ContentNews, News


class ContentNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentNews
        fields = ['id', 'image', 'title_photo', 'author_photo', 'date_photo']


class NewsSerializer(serializers.ModelSerializer):
    images = ContentNewsSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'description',
                  'date_published', 'images']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        content_news_instances = ContentNews.objects.filter(news=instance)
        images_data = ContentNewsSerializer(
            content_news_instances, many=True,
            context={'request': request}).data
        for image_data in images_data:
            image_data['image'] = request.build_absolute_uri(
                image_data['image'])

        representation['images'] = images_data
        return representation


class CoachSerializer(serializers.ModelSerializer):
    """
    Сериализатор дя вывода информации о тренерах.
    Выводятся все поля, за исключением birthday.
    """
    directions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Coach
        fields = ['surname', 'name', 'patronymic',
                  'achievements', 'directions', 'photo']
