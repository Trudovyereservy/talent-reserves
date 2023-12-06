from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from api.pagination import BlogPagination
from api.serializers import PostSerializer
from blog.models import Post, Tag, TagPost


@api_view()
def get_ok(request):
    '''
    Тестовый endpoint для SwaggerUI
    '''
    return Response({"message": "ok"})


class PostListViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с постами."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = BlogPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tags__name']

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_names = self.request.query_params.getlist('tags__name')

        if tag_names:
            tag_ids = Tag.objects.filter(name__in=tag_names).values_list(
                'id', flat=True)
            post_ids = TagPost.objects.filter(tag_id__in=tag_ids).values_list(
                'post_id', flat=True).distinct()
            queryset = queryset.filter(id__in=post_ids)

        return queryset
