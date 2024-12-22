from django.urls import path ,include
from .views import indexview
from django.views.generic import TemplateView
from .views import *
urlpatterns = [
    path('fbvindex',indexview, name = 'fbv_test'),
    path('post', PostList.as_view(), name = 'postlistt'),
    # path('cbvindex', TemplateView.as_view(template_name = 'base.html', extra_context = {"name" : "ali"}))
    path('cbvindex', HomeView.as_view() , name = 'cbv_index'),
]
