from rest_framework import generics
from apps.watchlist.models import UserDevice, Company, Watchlist
from .serializers import UserDeviceSerializer, CompanySerializer, WatchlistSerializer


class UserDeviceList(generics.ListCreateAPIView):
    queryset = UserDevice.objects.all()
    serializer_class = UserDeviceSerializer


class UserDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDevice.objects.all()
    serializer_class = UserDeviceSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class WatchlistList(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
