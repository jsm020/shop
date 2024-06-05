from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OyoqKiyimlarViewSet, OyoqKiyimRasmlariViewSet

router = DefaultRouter()
router.register(r'oyoqkiyimlar', OyoqKiyimlarViewSet)
router.register(r'oyoqkiyimlar-rasmlari', OyoqKiyimRasmlariViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
