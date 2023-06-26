from rest_framework import generics
from .filters import PriceFilter
from .models import City, Hotel, ApartmentType
from .serializer import CitySerializer, HotelSerializer, ApartmentTypeSerializer
from .pagination import PaginationList
from django_filters import rest_framework as filters


class CityListView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class HotelListView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    pagination_class = PaginationList
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_class = PriceFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filter_class(self.request.GET, queryset=queryset).qs


class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class ApartmentListView(generics.ListCreateAPIView):
    queryset = ApartmentType.objects.all()
    serializer_class = ApartmentType


class ApartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApartmentType.objects.all()
    serializer_class = ApartmentType
