from django.shortcuts import render

from .serializers import WomenSerializer
from .models import Women
from rest_framework import generics
# Create your views here.
class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    