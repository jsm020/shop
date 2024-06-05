from rest_framework import viewsets
from .models import Soatlar, Soatlar_rasmlari
from .serializers import SoatlarSerializer, SoatlarRasmlariSerializer

class SoatlarViewSet(viewsets.ModelViewSet):
    queryset = Soatlar.objects.all()
    serializer_class = SoatlarSerializer

class SoatlarRasmlariViewSet(viewsets.ModelViewSet):
    queryset = Soatlar_rasmlari.objects.all()
    serializer_class = SoatlarRasmlariSerializer
