from django.urls import path
from .views import CompanyProfileList,  CompanyTradingList, CompanyAdtvList, \
                   CompanyProfile, CompanyQuote, \
                   CompanyList, FmpDataList, IexDataList

app_name = 'company_api'

urlpatterns = [
    path('companies/<str:pk>/adtv', CompanyAdtvList.as_view(), name='company-adtv-list'),
    path('companies/<str:pk>/trading', CompanyTradingList.as_view(), name='company-trading-list'),
    path('companies/<str:pk>/quote', CompanyQuote.as_view(), name='company-quote'),
    path('companies/<str:pk>', CompanyProfile.as_view(), name='company-profile'),
    path('companies', CompanyProfileList.as_view(), name='company-profile-list'),

    path('company/list', CompanyList.as_view(), name='company-list-create'),
    path('company/fmp/list', FmpDataList.as_view(), name='fmp-data-list-create'),
    path('company/iex/list', IexDataList.as_view(), name='iex-data-list-create'),
]
