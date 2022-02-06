from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='blog-home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='blog-post-new'),
]