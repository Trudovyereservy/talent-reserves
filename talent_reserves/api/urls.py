from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import get_ok, PostListViewSet

router = SimpleRouter()

router.register('posts', PostListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('healthcheck/', get_ok, name='ok_endpoint')
]
