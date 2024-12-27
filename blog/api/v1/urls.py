from django.urls import path ,include
from . import views
app_name = 'api-v1'

urlpatterns = [
    path('post', views.PostList.as_view(), name='apipostlist'),
    path('post/<int:id>/', views.PostSingle.as_view(), name='apipostdetail'),
]
