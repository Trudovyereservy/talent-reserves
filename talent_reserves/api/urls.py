from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CoachViewSet, FeedbackViewSet, NewsViewSet,
                    PostListViewSet, get_ok)
app_name = 'api'
router = DefaultRouter()

router.register('coaches', CoachViewSet)
router.register('post', PostListViewSet)
router.register('news', NewsViewSet, basename='news')
router.register('feedback', FeedbackViewSet)

urlpatterns = [
    path('healthcheck/', get_ok, name='ok_endpoint'),
    path('', include(router.urls)),
]
