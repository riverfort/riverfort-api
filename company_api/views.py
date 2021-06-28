from rest_framework import generics
from company.models import CompanyProfile, CompanyQuote
from .serializers import CompanyProfileSerializer, CompanyQuoteSerializer


class CompanyProfileList(generics.ListAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyProfileDetail(generics.RetrieveAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyQuote(generics.RetrieveAPIView):
    queryset = CompanyQuote.objects.all()
    serializer_class = CompanyQuoteSerializer
