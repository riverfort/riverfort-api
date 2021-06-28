from django.urls import path
from .views import CompanyProfileList, CompanyProfile, CompanyQuote, CompanyTradingList, CompanyAdtvList

app_name = 'company_api'

urlpatterns = [
    path('companies/<str:pk>/adtv', CompanyAdtvList.as_view(), name='company-adtv-list'),
    path('companies/<str:pk>/trading', CompanyTradingList.as_view(), name='company-trading-list'),
    path('companies/<str:pk>/quote', CompanyQuote.as_view(), name='company-quote'),
    path('companies/<str:pk>', CompanyProfile.as_view(), name='company-profile'),
    path('companies', CompanyProfileList.as_view(), name='company-profile-list')
]
