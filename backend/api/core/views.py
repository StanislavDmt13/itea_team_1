from django.shortcuts import render
from rest_framework import generics

from db.models import Train

from . import serializers


class TrainsListView(generics.ListAPIView):

    queryset = Train.objects.all()
    serializer_class = serializers.TrainsListSerializer


class TrainView(generics.RetrieveAPIView):

    queryset = Train.objects.all()
    serializer_class = serializers.TrainSerializer



