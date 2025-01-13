from django.urls import path ,include
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('posts', views.PostList.as_view(), name='apipostlist'),
    path('posts/<int:id>/', views.PostSingle.as_view(), name='apipostdetail'),
    #path('post/',views.Postviewset.as_view({'get':'list'}), name='post-list'),
    #path('post/<int:pk>',views.Postviewset.as_view({'get':'retrieve'}), name='post-list'),


]
