from rest_framework import serializers
from company.models import CompanyProfile, CompanyQuote


class CompanyProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyProfile
        fields = ('company_ticker', 'company_name', 'exchange', 'currency', 'industry', 'sector', 'isin', 'country')


class CompanyQuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyQuote
        fields = ('company_ticker', 'market_cap', 'price', 'timestamp')
