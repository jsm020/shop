from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SumkalarViewSet, SumkalarRasmlariViewSet

router = DefaultRouter()
router.register(r'sumkalar', SumkalarViewSet)
router.register(r'sumkalar-rasmlari', SumkalarRasmlariViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
