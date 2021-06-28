from django.urls import path
from .views import CompanyProfileList, CompanyProfileDetail, CompanyQuote

app_name = 'company_api'

urlpatterns = [
    path('companies/<str:pk>/quote', CompanyQuote.as_view(), name='company-quote'),
    path('companies/<str:pk>', CompanyProfileDetail.as_view(), name='companyprofiledetail'),
    path('companies', CompanyProfileList.as_view(), name='companyprofilelist')
]
