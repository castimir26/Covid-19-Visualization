from django.shortcuts import render
from django.http import HttpResponse
from .models import Survived
from .serializers import SurvivedSerializer
from rest_framework import generics


class SurvivedListCreate(generics.ListCreateAPIView):
    queryset = Survived.objects.all()
    serializer_class = SurvivedSerializer
