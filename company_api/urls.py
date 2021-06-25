from django.urls import path
from .views import CompanyProfileList, CompanyProfileDetail

app_name = 'company_api'

urlpatterns = [
    path('<str:pk>/', CompanyProfileDetail.as_view(), name='companyprofiledetail'),
    path('', CompanyProfileList.as_view(), name='companyprofilelist')
]
