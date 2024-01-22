from rest_framework import serializers

from blog.models import ContentPost, Post, Tag
from coaches.models import Coach, Direction
from feedback.models import Feedback
from news.models import ContentNews, News


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)


class ContentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentPost
        fields = ('image',)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
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
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'tags',
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


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ['id', 'title']


class CoachSerializer(serializers.ModelSerializer):
    """
    Сериализатор дя вывода информации о тренерах.
    Выводятся все поля, за исключением birthday.
    """
    directions = DirectionSerializer(many=True, read_only=True)

    class Meta:
        model = Coach
        fields = ['id', 'surname', 'name', 'patronymic',
                  'achievements', 'directions', 'photo']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']
