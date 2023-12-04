from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PostListViewSet, get_ok

router = SimpleRouter()

router.register('posts', PostListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('healthcheck/', get_ok, name='ok_endpoint')
]
