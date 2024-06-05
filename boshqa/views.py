from rest_framework import viewsets
from .models import boshqa_mahuslot, boshqa_mahuslot_rasmlari
from .serializers import BoshqaMahuslotSerializer, BoshqaMahuslotRasmlariSerializer

class BoshqaMahuslotViewSet(viewsets.ModelViewSet):
    queryset = boshqa_mahuslot.objects.all()
    serializer_class = BoshqaMahuslotSerializer

class BoshqaMahuslotRasmlariViewSet(viewsets.ModelViewSet):
    queryset = boshqa_mahuslot_rasmlari.objects.all()
    serializer_class = BoshqaMahuslotRasmlariSerializer
