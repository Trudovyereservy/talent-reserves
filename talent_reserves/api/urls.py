from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import get_ok, CoachViewSet


router = DefaultRouter()
router.register('coaches', CoachViewSet)

urlpatterns = [
    path('healthcheck/', get_ok, name='ok_endpoint'),
    path('', include(router.urls)),
]
