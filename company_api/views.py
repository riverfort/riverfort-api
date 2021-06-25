from rest_framework import generics
from company.models import CompanyProfile
from .serializers import CompanyProfileSerializer


class CompanyProfileList(generics.ListAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyProfileDetail(generics.RetrieveAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
