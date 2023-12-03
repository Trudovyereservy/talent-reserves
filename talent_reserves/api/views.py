from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from api.serializers import PostSerializer
from api.pagination import BlogPagination


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
