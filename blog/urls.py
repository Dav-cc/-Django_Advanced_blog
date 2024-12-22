from django.urls import path ,include
from .views import indexview
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('fbvindex',indexview, name = 'fbv_test'),
    # path('cbvindex', TemplateView.as_view(template_name = 'base.html', extra_context = {"name" : "ali"}))
    path('cbvindex', views.HomeView.as_view() , name = 'cbv_index')
]
