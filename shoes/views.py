from rest_framework import viewsets
from .models import OyoqKiyimlar, OyoqKiyimRasmlari
from .serializers import OyoqKiyimlarSerializer, OyoqKiyimRasmlariSerializer

class OyoqKiyimlarViewSet(viewsets.ModelViewSet):
    queryset = OyoqKiyimlar.objects.all()
    serializer_class = OyoqKiyimlarSerializer

class OyoqKiyimRasmlariViewSet(viewsets.ModelViewSet):
    queryset = OyoqKiyimRasmlari.objects.all()
    serializer_class = OyoqKiyimRasmlariSerializer
