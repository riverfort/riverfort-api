from django.urls import path
from .views import CompanyProfileList,  CompanyTradingList, CompanyAdtvList, \
                   CompanyProfile, CompanyQuote, CompanyTradingQuote, CompanyAdtvQuote, \
                   CompanyList, FmpDataList, IexDataList, \
                   company_quote_full, \
                   add_company

app_name = 'company_api'

urlpatterns = [
    path('v1/companies/<str:pk>/trading/quote', CompanyTradingQuote.as_view(), name='company-trading-quote'),
    path('v1/companies/<str:pk>/adtv/quote', CompanyAdtvQuote.as_view(), name='company-adtv-quote'),
    path('v1/companies/<str:pk>/adtv', CompanyAdtvList.as_view(), name='company-adtv-list'),
    path('v1/companies/<str:pk>/trading', CompanyTradingList.as_view(), name='company-trading-list'),
    path('v1/companies/<str:pk>/quote', CompanyQuote.as_view(), name='company-quote'),
    path('v1/companies/<str:pk>', CompanyProfile.as_view(), name='company-profile'),
    path('v1/companies', CompanyProfileList.as_view(), name='company-profile-list'),

    path('v1/company/list', CompanyList.as_view(), name='company-list-create'),
    path('v1/company/list/fmp', FmpDataList.as_view(), name='fmp-list-create'),
    path('v1/company/list/iex', IexDataList.as_view(), name='iex-list-create'),
    path("v1/company/<str:ticker>/quote", company_quote_full, name='company-quote-full'),

    path('v1/add-on', add_company, name='add-on'),
]
