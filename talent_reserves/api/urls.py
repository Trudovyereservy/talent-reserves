from django.urls import path

from .views import get_ok


urlpatterns = [
    path('healthcheck/', get_ok, name='ok_endpoint'),
]
