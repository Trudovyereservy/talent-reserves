from blog.models import Post
from coaches.models import Coach
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from feedback.models import Feedback
from news.models import News
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from talent_reserves.tasks import send_feedback_email_task

from .filters import CoachFilter, NewsFilter, PostFilter
from .mixins import CreateViewSet
from .pagination import CommonPagination
from .serializers import (CoachSerializer, FeedbackSerializer, NewsSerializer,
                          PostSerializer)


class CoachViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для отображения информации о тренерах.
    Работает только на чтение (list, retrieve).
    Имеется фильтрация по полю slug модели Directions.
    """
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    pagination_class = CommonPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = CoachFilter


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения списка новостей."""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = CommonPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = NewsFilter

    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = News.objects.filter(date_published__lte=current_datetime)
        return queryset


class PostListViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с постами."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CommonPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = PostFilter


@api_view()
def get_ok(request):
    '''
    Тестовая вью-функция для SwaggerUI
    '''
    return Response({"message": "ok"})


class FeedbackViewSet(CreateViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    @receiver(post_save, sender=Feedback)
    def send_feedback_email(sender, instance, created, **kwargs):
        if created:
            send_feedback_email_task.delay()
            print(3, created)
