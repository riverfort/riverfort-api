from rest_framework import serializers
from apps.watchlist.models import DeviceTokens, Watchlist


class DeviceTokensSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceTokens
        fields = ('device_token',)


class WatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watchlist
        fields = ('device_token', 'company_symbol')
