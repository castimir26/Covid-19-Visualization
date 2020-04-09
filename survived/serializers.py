from rest_framework import serializers
from .models import Survived

class SurvivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survived
        fields = ('province', 'country','last_update','confirmed','deaths','recovered','active')
