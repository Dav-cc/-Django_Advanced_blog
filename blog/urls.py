from django.urls import path ,include
from .views import indexview
from django.views.generic import TemplateView

urlpatterns = [
    path('fbvindex',indexview, name = 'fbv_test'),
    path('cbvindex', TemplateView.as_view(template_name = 'base.html'))
]
