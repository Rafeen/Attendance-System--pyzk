from rest_framework import serializers
from .models import Device_user

class DeviceUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device_user
        fields = ('url', 'user_id', 'name', 'password')