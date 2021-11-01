from rest_framework import serializers
from django.contrib.auth.models import User

from .models import City, Cinema


class UserSerializer(serializers.HyperlinkedModelSerializer):
    PREFETCH_FIELDS = []
    RELATED_FIELDS = []

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'title']


class CinemaSerializer(serializers.ModelSerializer):
    PREFETCH_FIELDS = ['cinema']
    RELATED_FIELDS = ['city']

    class Meta:
        model = Cinema
        fields = '__all__'
