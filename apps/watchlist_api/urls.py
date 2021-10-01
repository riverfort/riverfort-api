from django.urls import path
from apps.watchlist_api import views

app_name = 'notification_api'

urlpatterns = [
    path('v1', views.WatchlistList.as_view(), name='watchlist'),
    path(
      'v1/device/<str:device_token>/company/<str:company_ticker>',
      views.WatchlistDetail.as_view(),
      name='watchlist-detail'),
    path('v1/device-tokens', views.DeviceTokensList.as_view(), name='device-token-list'),
    path('v1/device-tokens/<str:pk>', views.DeviceTokenDetail.as_view(), name='device-token-detail'),
]
