from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.company.models import CompanyProfile, CompanyQuote, CompanyTrading, CompanyAdtv, Company, FmpData, IexData
from apps.company_api.models import Company_Profile
from .serializers import CompanyProfileSerializer, CompanyQuoteSerializer, \
                         CompanyTradingSerializer, CompanyAdtvSerializer, \
                         CompanySerializer, FmpDataSerializer, IexDataSerializer, \
                         Companies_Quotes_Trading_ADTV_Serializer


class DynamicFieldsViewMixin(object):

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()

        fields = None
        if self.request.method == 'GET':
            query_fields = self.request.query_params.get("fields", None)

            if query_fields:
                fields = tuple(query_fields.split(','))

        kwargs['context'] = self.get_serializer_context()
        kwargs['fields'] = fields

        return serializer_class(*args, **kwargs)


class CompanyProfileList(DynamicFieldsViewMixin, generics.ListAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['company_name']


class CompanyProfile(DynamicFieldsViewMixin, generics.RetrieveAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyQuote(DynamicFieldsViewMixin, generics.RetrieveAPIView):
    queryset = CompanyQuote.objects.all()
    serializer_class = CompanyQuoteSerializer


class CompanyTradingList(DynamicFieldsViewMixin, generics.ListAPIView):
    serializer_class = CompanyTradingSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['market_date']

    def get_queryset(self):
        company_ticker = self.kwargs['pk']
        return CompanyTrading.objects.filter(company_ticker=company_ticker)


class CompanyAdtvList(DynamicFieldsViewMixin, generics.ListAPIView):
    serializer_class = CompanyAdtvSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']

    def get_queryset(self):
        company_ticker = self.kwargs['pk']
        return CompanyAdtv.objects.filter(company_ticker=company_ticker)


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class FmpDataList(generics.ListCreateAPIView):
    queryset = FmpData.objects.all()
    serializer_class = FmpDataSerializer


class IexDataList(generics.ListCreateAPIView):
    queryset = IexData.objects.all()
    serializer_class = IexDataSerializer


class CompanyTradingQuote(APIView):

    def get(self, request, pk, format=None):
        company_trading_quote = CompanyTrading.objects.filter(company_ticker=pk).order_by('-market_date').first()
        serializer = CompanyTradingSerializer(company_trading_quote, many=False)
        return Response(serializer.data)


class CompanyAdtvQuote(APIView):

    def get(self, request, pk, format=None):
        company_adtv_quote = CompanyAdtv.objects.filter(company_ticker=pk).order_by('-date').first()
        serializer = CompanyAdtvSerializer(company_adtv_quote, many=False)
        return Response(serializer.data)


@api_view(['GET'])
def company_quote_full(request, ticker):
    companies = Company_Profile.objects.raw(
        """
        SELECT * FROM company_profile
        LEFT JOIN company_quote ON company_profile.company_ticker=company_quote.company_ticker
        LEFT JOIN (SELECT c.company_ticker, c.market_date, c.open, c.close,
        c.high, c.low, c.vwap, c.volume, c.change_percent FROM company_trading c
        INNER JOIN (SELECT company_ticker, MAX(market_date) as MaxDate FROM company_trading GROUP BY company_ticker) cm
        ON c.company_ticker=cm.company_ticker AND c.market_date=cm.MaxDate) t
        ON company_profile.company_ticker=t.company_ticker
        LEFT JOIN (SELECT a.company_ticker, a.date, a.adtv, a.adtv5, a.adtv10, a.adtv20, a.adtv60, a.adtv120,
        a.isoutlier, a.aadtv, a.aadtv5, a.aadtv10, a.aadtv20, a.aadtv60, a.aadtv120 FROM company_adtv a
        INNER JOIN (SELECT company_ticker, MAX(date) as MaxDate FROM company_adtv GROUP BY company_ticker) am
        ON a.company_ticker=am.company_ticker AND a.date=am.MaxDate) a
        ON company_profile.company_ticker=a.company_ticker WHERE company_profile.company_ticker=%s;
        """, [ticker])
    serializer = Companies_Quotes_Trading_ADTV_Serializer(companies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_company(request):
    from company_api.serializers import AddOnCompanySerializer
    serializer = AddOnCompanySerializer(data=request.data)
    if serializer.is_valid():
        validatedData = serializer.validated_data
        company_ticker = validatedData.get('company_ticker')
        company_name = validatedData.get('company_name')
        if Company.objects.filter(symbol=company_ticker).exists():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            from django.db import connections
            from company_api.db_utils import insert_add_on_company, insert_company_profile, \
                insert_company_quote, insert_company_trading, insert_company_adtv
            cursor = connections['companies_db'].cursor()
            insert_add_on_company(cursor, company_ticker, company_name)
            insert_company_profile(cursor, company_ticker)
            insert_company_quote(cursor, company_ticker)
            insert_company_trading(cursor, company_ticker)
            insert_company_adtv(cursor, company_ticker)
            return Response({"message": "Added to database"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
