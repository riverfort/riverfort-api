from django.urls import path
from .views import UserDeviceList, CompanyList, WatchlistList

app_name = 'notification_api'

urlpatterns = [
    path('v1/user-devices', UserDeviceList.as_view(), name='user-devices'),
    path('v1/companies', CompanyList.as_view(), name='companies'),
    path('v1/watchlist', WatchlistList.as_view(), name='watchlist'),
]
