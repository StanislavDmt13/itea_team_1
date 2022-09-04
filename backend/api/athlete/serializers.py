from rest_framework import serializers
from db.models import User, Train


class TrainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = ['id', 'title', 'description', 'image', 'author', 'train_program']


class AthleteSerializer(serializers.ModelSerializer):

    trains = TrainSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthday', 'phone', 'email', 'trains']

