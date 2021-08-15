from django.urls import path
from apps.watchlist_api import views

app_name = 'notification_api'

urlpatterns = [
    path('v1', views.WatchlistList.as_view(), name='watchlist'),
    path(
      'v1/device/<str:device_toke>/company/<str:company_ticker>',
      views.WatchlistDetail.as_view(),
      name='watchlist-detail'),
    path('v1/user-devices', views.UserDeviceList.as_view(), name='user-devices-list'),
    path('v1/user-devices/<str:pk>', views.UserDeviceDetail.as_view(), name='user-device-detail'),
    path('v1/companies', views.CompanyList.as_view(), name='companies-list'),
]
