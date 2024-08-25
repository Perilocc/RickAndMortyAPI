from rest_framework.routers import DefaultRouter
from .viewsets import RickAndMortyViewSet

router = DefaultRouter()

router.register(r'RickAndMortyAPI', RickAndMortyViewSet)

urlpatterns = router.urls