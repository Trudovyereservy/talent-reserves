from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import NewsViewSet

from .views import get_ok

router = DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('healthcheck/', get_ok, name='ok_endpoint'),
    path('', include(router.urls)),
]
