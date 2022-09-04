from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from db.models import User, Train
from . import serializers


class AthleteView(generics.RetrieveUpdateAPIView):

    permissions_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.AthleteSerializer

    def get_object(self):
        return self.request.user


class TrainAddView(generics.CreateAPIView):

    permissions_classes = (IsAuthenticated,)
    queryset = Train.objects.all()
    serializer_class = serializers.TrainSerializer


class TrainEditView(generics.RetrieveUpdateAPIView):

    permissions_classes = (IsAuthenticated,)
    queryset = Train.objects.all()
    serializer_class = serializers.TrainSerializer


class TrainDeleteView(generics.DestroyAPIView):

    permissions_classes = (IsAuthenticated,)
    queryset = Train.objects.all()
    serializer_class = serializers.TrainSerializer

