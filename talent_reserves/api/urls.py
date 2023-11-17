from rest_framework import routers

from .views import GetOkView


router = routers.SimpleRouter()
router.register('healthcheck/', GetOkView, basename='get_ok')

urlpatterns = router.urls
