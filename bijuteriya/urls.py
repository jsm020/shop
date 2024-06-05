from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaqinchoqlarViewSet, TaqinchoqlarRasmlariViewSet

router = DefaultRouter()
router.register(r'taqinchoqlar', TaqinchoqlarViewSet)
router.register(r'taqinchoqlar-rasmlari', TaqinchoqlarRasmlariViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
