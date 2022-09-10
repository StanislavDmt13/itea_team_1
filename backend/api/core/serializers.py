from rest_framework import serializers

from db.models import User, Train, TrainProgram


class AuthorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']


class TrainProgramNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainProgram
        fields = ['name']


class TrainsListSerializer(serializers.ModelSerializer):

    author = AuthorListSerializer(many=False, read_only=True)
    train_program = TrainProgramNameSerializer(many=False, read_only=True)

    class Meta:
        model = Train
        fields = ['id', 'title', 'description', 'image', 'author', 'train_program']


class TrainSerializer(serializers.ModelSerializer):

    author = AuthorListSerializer(many=False, read_only=True)
    train_program = TrainProgramNameSerializer(many=False, read_only=True)

    class Meta:
        model = Train
        fields = ['id', 'title', 'description', 'image', 'author', 'train_program']
