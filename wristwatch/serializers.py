from rest_framework import serializers
from .models import Soatlar, Soatlar_rasmlari

class SoatlarRasmlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soatlar_rasmlari
        fields = '__all__'

class SoatlarSerializer(serializers.ModelSerializer):
    Soatlar = SoatlarRasmlariSerializer(many=True, read_only=True)

    class Meta:
        model = Soatlar
        fields = '__all__'
