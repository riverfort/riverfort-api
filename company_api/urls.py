from django.urls import path
from .views import CompanyProfileList,  CompanyTradingList, CompanyAdtvList, \
                   CompanyProfile, CompanyQuote, CompanyTradingQuote, CompanyAdtvQuote, \
                   CompanyList, FmpDataList, IexDataList, \
                   add_company, \
                   company_all_data

app_name = 'company_api'

urlpatterns = [
    path('companies/<str:pk>/trading/quote', CompanyTradingQuote.as_view(), name='company-trading-quote'),
    path('companies/<str:pk>/adtv/quote', CompanyAdtvQuote.as_view(), name='company-adtv-quote'),
    path('companies/<str:pk>/adtv', CompanyAdtvList.as_view(), name='company-adtv-list'),
    path('companies/<str:pk>/trading', CompanyTradingList.as_view(), name='company-trading-list'),
    path('companies/<str:pk>/quote', CompanyQuote.as_view(), name='company-quote'),
    path('companies/<str:pk>', CompanyProfile.as_view(), name='company-profile'),
    path('companies', CompanyProfileList.as_view(), name='company-profile-list'),

    path('company/list', CompanyList.as_view(), name='company-list-create'),
    path('company/list/fmp', FmpDataList.as_view(), name='fmp-list-create'),
    path('company/list/iex', IexDataList.as_view(), name='iex-list-create'),

    path('add-on', add_company, name="add-on"),

    path("company-detail/<str:company_ticker>", company_all_data, name="company_all_data"),
]
