from django.urls import path, include

from .views import get_ok
from rest_framework.routers import DefaultRouter
from api.views import NewsViewSet

router = DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('healthcheck/', get_ok, name='ok_endpoint'),
    path('api/', include(router.urls)),
]
