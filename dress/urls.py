from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AyollarKoylagiViewSet, AyollarKoylagiRasmlariViewSet,dress_list


router = DefaultRouter()
router.register(r'ayollar-koylagi', AyollarKoylagiViewSet)
router.register(r'ayollar-koylagi-rasmlari', AyollarKoylagiRasmlariViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/',dress_list, name='product_list'),

]
