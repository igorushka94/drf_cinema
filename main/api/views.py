from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import City, Cinema
from .serializers import CitySerializer, CinemaSerializer, CityListSerializers


class CityCreateAPIView(generics.CreateAPIView):
    serializer_class = CitySerializer


class CityListView(generics.ListCreateAPIView):
    serializer_class = CityListSerializers
    queryset = City.objects.all()


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CinemaRetrieveAPIView(generics.RetrieveAPIView):
    """
    Выводит иформацию о всех кинотеатрах
    """
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class TestAPIView(APIView):

    def get(self):
        cinema = Cinema.objects.all()
        data = {
            'c': cinema.address,
        }
        return Response(data=data, status=200)


@api_view(http_method_names=['GET'])
def test(request):
    return Response({'message': 'hello'})
