from rest_framework import serializers

from blog.models import Post, ContentPost, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class ContentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentPost
        fields = ('image',)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    images = ContentPostSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_images(self, obj):
        content_posts = obj.images.all()
        serializer = ContentPostSerializer(content_posts, many=True)
        return [item['image'].name for item in serializer.data]
