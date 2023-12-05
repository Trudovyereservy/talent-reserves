from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('doc/', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(
        url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
