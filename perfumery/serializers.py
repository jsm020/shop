from rest_framework import serializers
from .models import Parfemeriya, Parfemeriya_rasmlari

class ParfemeriyaRasmlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parfemeriya_rasmlari
        fields = '__all__'

class ParfemeriyaSerializer(serializers.ModelSerializer):
    Parfemeriya = ParfemeriyaRasmlariSerializer(many=True, read_only=True)

    class Meta:
        model = Parfemeriya
        fields = '__all__'
