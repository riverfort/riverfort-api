from rest_framework import generics
from apps.watchlist.models import DeviceTokens, Watchlist
from .serializers import DeviceTokensSerializer, WatchlistSerializer


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


class UserDeviceList(generics.ListCreateAPIView):
    queryset = DeviceTokens.objects.all()
    serializer_class = DeviceTokensSerializer


class UserDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceTokens.objects.all()
    serializer_class = DeviceTokensSerializer


class WatchlistList(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer


class WatchlistDetail(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    lookup_fields = ['device_token', 'company_symbol']
