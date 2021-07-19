from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('company.urls', namespace='company')),
    path('api/', include('company_api.urls', namespace='company_api')),
    path('schema', get_schema_view(
        title="RiverFort REST API",
        description="Equity API",
        version="1.0.0",
    ), name='openapi-schema')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
