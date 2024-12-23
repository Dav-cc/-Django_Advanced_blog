from django.urls import path ,include
from .views import indexview
from django.views.generic import TemplateView
from .views import *

app_name = 'blog'

urlpatterns = [
    path('fbvindex',indexview, name = 'fbv_test'),
    path('post', PostList.as_view(), name = 'postlistt'),
    path('cbvindex', HomeView.as_view() , name = 'cbv_index'),
    path('posts/<int:pk>' , PostDetailView.as_view(), name = 'detail'),
    path('formpost', PostCreatFormView.as_view(), name = 'form')
]
