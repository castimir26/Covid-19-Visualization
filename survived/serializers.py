from rest_framework import serializers
from .models import Survived, World

class SurvivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survived
        fields = ('province', 'country','last_update','confirmed','deaths','recovered','active')

class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ('updated', 'confirmed', 'recovered', 'deaths', 'active')
