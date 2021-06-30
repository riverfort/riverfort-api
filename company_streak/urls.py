from django.urls import path
from django.views.generic import TemplateView

app_name = 'company_streak'

urlpatterns = [
    path('', TemplateView.as_view(template_name='company/index.html')),
]
