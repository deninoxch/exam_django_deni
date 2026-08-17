from django.shortcuts import render
from rest_framework import viewsets
from .models import Men
from .serializers import MenSerializer


class MenViewSet(viewsets.ModelViewSet):
    queryset = Men.objects.all()
    serializer_class = MenSerializer