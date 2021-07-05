from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('company.urls', namespace='company')),
    path('api/', include('company_api.urls', namespace='company_api')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
