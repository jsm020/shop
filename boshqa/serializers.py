from rest_framework import serializers
from .models import boshqa_mahuslot, boshqa_mahuslot_rasmlari

class BoshqaMahuslotRasmlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = boshqa_mahuslot_rasmlari
        fields = '__all__'

class BoshqaMahuslotSerializer(serializers.ModelSerializer):
    Boshqa = BoshqaMahuslotRasmlariSerializer(many=True, read_only=True)

    class Meta:
        model = boshqa_mahuslot
        fields = '__all__'
