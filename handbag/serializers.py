from rest_framework import serializers
from .models import Sumkalar, Sumkalar_rasmlari

class SumkalarRasmlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sumkalar_rasmlari
        fields = '__all__'

class SumkalarSerializer(serializers.ModelSerializer):
    Sumkalar = SumkalarRasmlariSerializer(many=True, read_only=True)

    class Meta:
        model = Sumkalar
        fields = '__all__'
