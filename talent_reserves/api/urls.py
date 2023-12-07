from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CoachViewSet, NewsViewSet, get_ok


router = DefaultRouter()

router.register('coaches', CoachViewSet)
router.register('news', NewsViewSet, basename='news')

urlpatterns = [
    path('healthcheck/', get_ok, name='ok_endpoint'),
    path('', include(router.urls)),
]
