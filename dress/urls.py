from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AyollarKoylagiViewSet, AyollarKoylagiRasmlariViewSet

router = DefaultRouter()
router.register(r'ayollar-koylagi', AyollarKoylagiViewSet)
router.register(r'ayollar-koylagi-rasmlari', AyollarKoylagiRasmlariViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
