from django.urls import path ,include
from . import views
app_name = 'api-v1'

urlpatterns = [
    path('post', views.postList, name='apipostlist'),
    path('post/<int:id>/', views.postDetail, name='apipostdetail'),
]
