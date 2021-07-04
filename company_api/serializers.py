from rest_framework import serializers
from company.models import CompanyProfile, CompanyQuote, CompanyTrading, CompanyAdtv, Company, FmpData, IexData


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class CompanyProfileSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = CompanyProfile
        fields = ('company_ticker', 'company_name', 'exchange', 'currency', 'industry', 'sector', 'isin', 'country')


class CompanyQuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyQuote
        fields = ('company_ticker', 'market_cap', 'price', 'timestamp')


class CompanyTradingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyTrading
        fields = ('company_ticker', 'market_date', 'open', 'close', 'high', 'low', 'vwap', 'volume', 'change_percent')


class CompanyAdtvSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyAdtv
        fields = ('company_ticker', 'date', 'adtv', 'adtv5', 'adtv10', 'adtv20', 'adtv60', 'adtv120',
                  'isoutlier', 'aadtv', 'aadtv5', 'aadtv10', 'aadtv20', 'aadtv60', 'aadtv120')


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('name', 'symbol', 'am_name', 'am_email', 'status', 'isstreak', 'isaddon')


class FmpDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = FmpData
        fields = ('id', 'symbol', 'name', 'currency', 'exchange', 'short_exchange')


class IexDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = IexData
        fields = ('id', 'symbol', 'cik', 'exchange', 'securityname', 'securitytype', 'region', 'sector')
