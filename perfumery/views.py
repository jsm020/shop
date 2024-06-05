from rest_framework import viewsets
from .models import Parfemeriya, Parfemeriya_rasmlari
from .serializers import ParfemeriyaSerializer, ParfemeriyaRasmlariSerializer

class ParfemeriyaViewSet(viewsets.ModelViewSet):
    queryset = Parfemeriya.objects.all()
    serializer_class = ParfemeriyaSerializer

class ParfemeriyaRasmlariViewSet(viewsets.ModelViewSet):
    queryset = Parfemeriya_rasmlari.objects.all()
    serializer_class = ParfemeriyaRasmlariSerializer
