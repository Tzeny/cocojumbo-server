from rest_framework import serializers
from cocojumbo_server.models import User,Camera,Alert


class CameraSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    cameras = CameraSerializer(many=True, required=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password',instance.password)
        instance.email = validated_data.get('password',instance.email)
        instance.cameras = validated_data.get('cameras', instance.cameras)

        instance.save()
        return instance
