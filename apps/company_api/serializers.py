from rest_framework import serializers
from apps.company.models import CompanyProfile, CompanyQuote, CompanyTrading, CompanyAdtv, Company, FmpData, IexData
from apps.company_api.models import AddOnCompany


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


class CompanyQuoteSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = CompanyQuote
        fields = ('company_ticker', 'market_cap', 'price', 'timestamp')


class CompanyTradingSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = CompanyTrading
        fields = ('company_ticker', 'market_date', 'open', 'close', 'high', 'low', 'vwap', 'volume', 'change_percent')


class CompanyAdtvSerializer(DynamicFieldsModelSerializer):

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


class AddOnCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = AddOnCompany
        fields = ('company_ticker', 'company_name')


class Companies_Quotes_Trading_ADTV_Serializer(serializers.Serializer):
    company_ticker = serializers.CharField(max_length=25)
    company_name = serializers.CharField(max_length=100)
    exchange = serializers.CharField(max_length=100)
    exchange_type = serializers.CharField(max_length=25)
    currency = serializers.CharField(max_length=5)
    industry = serializers.CharField(max_length=100)
    sector = serializers.CharField(max_length=100)
    isin = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)
    normalizer = serializers.IntegerField()
    am_uid = serializers.CharField()
    created_date = serializers.DateTimeField()
    market_cap = serializers.FloatField()
    price = serializers.FloatField()
    timestamp = serializers.DateTimeField()
    market_date = serializers.DateField()
    open = serializers.FloatField()
    close = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    vwap = serializers.FloatField()
    volume = serializers.FloatField()
    change_percent = serializers.FloatField()
    date = serializers.DateField()
    adtv = serializers.FloatField()
    adtv5 = serializers.FloatField()
    adtv10 = serializers.FloatField()
    adtv20 = serializers.FloatField()
    adtv60 = serializers.FloatField()
    adtv120 = serializers.FloatField()
    isoutlier = serializers.BooleanField()
    aadtv = serializers.FloatField()
    aadtv5 = serializers.DecimalField(max_digits=19, decimal_places=0)
    aadtv10 = serializers.DecimalField(max_digits=19, decimal_places=0)
    aadtv20 = serializers.DecimalField(max_digits=19, decimal_places=0)
    aadtv60 = serializers.DecimalField(max_digits=19, decimal_places=0)
    aadtv120 = serializers.DecimalField(max_digits=19, decimal_places=0)
