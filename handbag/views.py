from rest_framework import viewsets
from .models import Sumkalar, Sumkalar_rasmlari
from .serializers import SumkalarSerializer, SumkalarRasmlariSerializer

class SumkalarViewSet(viewsets.ModelViewSet):
    queryset = Sumkalar.objects.all()
    serializer_class = SumkalarSerializer

class SumkalarRasmlariViewSet(viewsets.ModelViewSet):
    queryset = Sumkalar_rasmlari.objects.all()
    serializer_class = SumkalarRasmlariSerializer
