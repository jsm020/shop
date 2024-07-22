from rest_framework import viewsets
from handbag.models import Sumkalar
from .models import AyollarKoylagi, AyollarKoylagiRasmlari
from .serializers import AyollarKoylagiSerializer, AyollarKoylagiRasmlariSerializer
from django.shortcuts import render

def dress_list(request):
    dress = AyollarKoylagi.objects.all()
    handbags = Sumkalar.objects.all()
    return render(request, 'shop/product-list.html', {'dress': dress, 'handbags':handbags})


class AyollarKoylagiViewSet(viewsets.ModelViewSet):
    queryset = AyollarKoylagi.objects.all()
    serializer_class = AyollarKoylagiSerializer

class AyollarKoylagiRasmlariViewSet(viewsets.ModelViewSet):
    queryset = AyollarKoylagiRasmlari.objects.all()
    serializer_class = AyollarKoylagiRasmlariSerializer
