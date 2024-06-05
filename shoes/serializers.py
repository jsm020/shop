from rest_framework import serializers
from .models import OyoqKiyimlar, OyoqKiyimRasmlari

class OyoqKiyimRasmlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = OyoqKiyimRasmlari
        fields = '__all__'

class OyoqKiyimlarSerializer(serializers.ModelSerializer):
    Oyoq_Kiyimlar = OyoqKiyimRasmlariSerializer(many=True, read_only=True)

    class Meta:
        model = OyoqKiyimlar
        fields = '__all__'
