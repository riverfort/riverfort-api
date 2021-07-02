from rest_framework import generics
from company.models import CompanyProfile, CompanyQuote, CompanyTrading, CompanyAdtv, Company, FmpData, IexData
from .serializers import CompanyProfileSerializer, CompanyQuoteSerializer, \
                         CompanyTradingSerializer, CompanyAdtvSerializer, \
                         CompanySerializer, FmpDataSerializer, IexDataSerializer


class CompanyProfileList(generics.ListAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyProfile(generics.RetrieveAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyQuote(generics.RetrieveAPIView):
    queryset = CompanyQuote.objects.all()
    serializer_class = CompanyQuoteSerializer


class CompanyTradingList(generics.ListAPIView):
    serializer_class = CompanyTradingSerializer

    def get_queryset(self):
        company_ticker = self.kwargs['pk']
        return CompanyTrading.objects.filter(company_ticker=company_ticker)


class CompanyAdtvList(generics.ListAPIView):
    serializer_class = CompanyAdtvSerializer

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
