from rest_framework import viewsets
from .models import AyollarKoylagi, AyollarKoylagiRasmlari
from .serializers import AyollarKoylagiSerializer, AyollarKoylagiRasmlariSerializer

class AyollarKoylagiViewSet(viewsets.ModelViewSet):
    queryset = AyollarKoylagi.objects.all()
    serializer_class = AyollarKoylagiSerializer

class AyollarKoylagiRasmlariViewSet(viewsets.ModelViewSet):
    queryset = AyollarKoylagiRasmlari.objects.all()
    serializer_class = AyollarKoylagiRasmlariSerializer
