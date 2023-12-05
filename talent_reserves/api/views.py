from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from coaches.models import Coach
from .serializers import CoachSerializer
from .pagination import CoachPagination


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


@api_view()
def get_ok(request):
    '''
    Тестовая вью-функция для SwaggerUI
    '''
    return Response({"message": "ok"})
