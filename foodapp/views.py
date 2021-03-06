from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FoodSerializer
# Create your views here.
from .models import Foods
import django_filters
from rest_framework import generics
# from django_filters import rest_framework as filters

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FoodSerializer

class SweetViewSet(viewsets.ModelViewSet):
    queryset = Foods.objects.filter(typ='sweet')    
    serializer_class = FoodSerializer

class SpicyViewSet(viewsets.ModelViewSet):
    queryset = Foods.objects.filter(typ='Spicy')    
    serializer_class = FoodSerializer


class RateFilter(django_filters.FilterSet):
    rate = django_filters.NumberFilter()
    price_greater = django_filters.NumberFilter(field_name='rate', lookup_expr='gt')
    price_lesser = django_filters.NumberFilter(field_name='rate', lookup_expr='lt')
    class Meta:
        model = Foods
        fields = [ 'price_greater', 'price_lesser']

class RateViewSet(generics.ListAPIView):
    queryset = Foods.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [DjangoFilterBackend,]
    # filterset_fields = ['rate']
    filter_class = RateFilter

   



