from django.urls import path
from apps.notification_api import views

app_name = 'notification_api'

urlpatterns = [
    path('v1/user-devices', views.UserDeviceList.as_view(), name='user-devices-list'),
    path('v1/user-devices/<str:pk>', views.UserDeviceDetail.as_view(), name='user-device-detail'),
    path('v1/companies', views.CompanyList.as_view(), name='companies-list'),
    path('v1/watchlist', views.WatchlistList.as_view(), name='watchlist-list'),
]
