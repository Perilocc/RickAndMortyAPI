from django.shortcuts import render
from .serializers import TesteSerializer, TesteCampos
from rest_framework import viewsets
# Create your views here.

class TesteViewSet(viewsets.ModelViewSet):
    queryset = TesteCampos.objects.all()
    serializer_class = TesteSerializer
