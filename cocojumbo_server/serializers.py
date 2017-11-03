from rest_framework import serializers
from cocojumbo_server.models import User,Camera,Alert


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    cameras = CameraSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'cameras')


class AlertSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = Alert
        fields = ('id', 'timestamp', 'user', 'message')