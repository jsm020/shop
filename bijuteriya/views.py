from rest_framework import viewsets
from .models import Taqinchoqlar, Taqinchoqlar_rasmlari
from .serializers import TaqinchoqlarSerializer, TaqinchoqlarRasmlariSerializer

class TaqinchoqlarViewSet(viewsets.ModelViewSet):
    queryset = Taqinchoqlar.objects.all()
    serializer_class = TaqinchoqlarSerializer

class TaqinchoqlarRasmlariViewSet(viewsets.ModelViewSet):
    queryset = Taqinchoqlar_rasmlari.objects.all()
    serializer_class = TaqinchoqlarRasmlariSerializer
