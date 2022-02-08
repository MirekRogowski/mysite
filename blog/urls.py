from django.urls import path
from . import views


urlpatterns = [
    path('', views.HoneView.as_view(), name='blog-home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post-add/', views.AddPostView.as_view(), name='post-add'),
    path('post-update/<int:pk>', views.UpdatePostView.as_view(), name='post-update'),

    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='blog-post-new'),
]