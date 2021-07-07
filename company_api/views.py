from rest_framework import generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from company.models import CompanyProfile, CompanyQuote, CompanyTrading, CompanyAdtv, Company, FmpData, IexData
from .serializers import CompanyProfileSerializer, CompanyQuoteSerializer, \
                         CompanyTradingSerializer, CompanyAdtvSerializer, \
                         CompanySerializer, FmpDataSerializer, IexDataSerializer


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
