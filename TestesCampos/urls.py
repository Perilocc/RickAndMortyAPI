from rest_framework.routers import DefaultRouter
from .views import TesteViewSet

router = DefaultRouter()

router.register(r'', TesteViewSet)

urlpatterns = router.urls