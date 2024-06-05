from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SoatlarViewSet, SoatlarRasmlariViewSet

router = DefaultRouter()
router.register(r'soatlar', SoatlarViewSet)
router.register(r'soatlar-rasmlari', SoatlarRasmlariViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
