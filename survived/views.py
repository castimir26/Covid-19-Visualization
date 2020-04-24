from django.shortcuts import render
from django.http import HttpResponse
from .models import Survived, World
from .serializers import SurvivedSerializer, WorldSerializer
from rest_framework import generics
from rest_framework import filters


class SurvivedListCreate(generics.ListCreateAPIView):
    search_fields = ['country','province']
    filter_backends = (filters.SearchFilter,)
    queryset = Survived.objects.all()
    serializer_class = SurvivedSerializer

class WorldListCreate(generics.ListCreateAPIView):
    queryset = World.objects.all()
    serializer_class = WorldSerializer
