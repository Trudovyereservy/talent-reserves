from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from coaches.models import Coach
from news.models import News
from .serializers import CoachSerializer, NewsSerializer
from .pagination import CoachPagination, NewsPagination


class CoachViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для отображения информации о тренерах.
    Работает только на чтение (list, retrieve).
    Имеется фильтрация по полю slug модели Directions.
    """
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['directions__slug',]
    pagination_class = CoachPagination

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения списка новостей."""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination

    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = News.objects.filter(date_published__lte=current_datetime)
        return queryset

      
@api_view()
def get_ok(request):
    '''
    Тестовая вью-функция для SwaggerUI
    '''
    return Response({"message": "ok"})
