from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NewsSerializer
from rest_framework import viewsets, permissions
from news.models import News
from .pagination import NewsPagination


@api_view()
def get_ok(request):
    '''
    Тестовый endpoint для SwaggerUI
    '''
    return Response({"message": "ok"})


class NewsViewSet(viewsets.ModelViewSet):
    """Вьюсет для списка новостей."""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        else:
            return (permissions.IsAdminUser(),)
