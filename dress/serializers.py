from rest_framework import serializers
from .models import AyollarKoylagi, AyollarKoylagiRasmlari

class AyollarKoylagiRasmlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = AyollarKoylagiRasmlari
        fields = '__all__'

class AyollarKoylagiSerializer(serializers.ModelSerializer):
    Ayollar_koylagi = AyollarKoylagiRasmlariSerializer(many=True, read_only=True)

    class Meta:
        model = AyollarKoylagi
        fields = '__all__'
