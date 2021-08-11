from rest_framework import serializers
from apps.notification.models import UserDevice, Company, Watchlist


class UserDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDevice
        fields = ('device_id',)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('company_ticker', 'company_name')


class WatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watchlist
        fields = ('device', 'company_ticker')
