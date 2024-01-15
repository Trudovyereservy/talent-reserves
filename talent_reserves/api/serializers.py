from blog.models import ContentPost, Post
from coaches.models import Coach
from news.models import ContentNews, News
from rest_framework import serializers


class ContentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentPost
        fields = ('image',)


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    images = ContentPostSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        exclude = ('created_at', 'updated_at')

    def get_images(self, obj):
        content_posts = obj.images.all()
        serializer = ContentPostSerializer(content_posts, many=True)
        return [item['image'].name for item in serializer.data]

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]


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
