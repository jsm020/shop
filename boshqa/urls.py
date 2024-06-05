from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoshqaMahuslotViewSet, BoshqaMahuslotRasmlariViewSet

router = DefaultRouter()
router.register(r'boshqa-mahuslot', BoshqaMahuslotViewSet)
router.register(r'boshqa-mahuslot-rasmlari', BoshqaMahuslotRasmlariViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
