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


class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.

    Source: https://www.django-rest-framework.org/api-guide/generic-views/#creating-custom-mixins
    Modified to not error out for not providing all fields in the url.
    """
    def get_object(self):
        from django.shortcuts import get_object_or_404
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field):  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class WatchlistDetail(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    lookup_fields = ['device', 'company_ticker']
