from rest_framework import serializers
from .models import Taqinchoqlar, Taqinchoqlar_rasmlari

class TaqinchoqlarRasmlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taqinchoqlar_rasmlari
        fields = '__all__'

class TaqinchoqlarSerializer(serializers.ModelSerializer):
    Taqinchoqlar = TaqinchoqlarRasmlariSerializer(many=True, read_only=True)

    class Meta:
        model = Taqinchoqlar
        fields = '__all__'
