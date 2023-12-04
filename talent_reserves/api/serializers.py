from rest_framework import serializers

from blog.models import Post, ContentPost, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ContentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentPost
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    images = ContentPostSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
