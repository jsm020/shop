from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParfemeriyaViewSet, ParfemeriyaRasmlariViewSet

router = DefaultRouter()
router.register(r'parfemeriya', ParfemeriyaViewSet)
router.register(r'parfemeriya-rasmlari', ParfemeriyaRasmlariViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
