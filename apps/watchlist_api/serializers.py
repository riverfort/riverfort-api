from rest_framework import serializers
from apps.watchlist.models import UserDevice, Company, Watchlist


class UserDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDevice
        fields = ('device_token',)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('company_ticker', 'company_name')


class WatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watchlist
        fields = ('device_token', 'company_ticker')
