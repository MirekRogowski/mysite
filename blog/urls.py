from django.urls import path
from . import views


urlpatterns = [
    path('', views.HoneView.as_view(), name='blog-home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post-add/', views.AddPostView.as_view(), name='post-add'),
    path('post-update/<int:pk>', views.UpdatePostView.as_view(), name='post-update'),
    path('post-delete/<int:pk>', views.DeletePostView.as_view(), name='post-delete'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category-add/', views.AddCategoryView.as_view(), name='category-add'),
    # path('category-post/<str:category>/', views.post_category_view, name='category-post'),
    # path('category-post/<str:category>/', views.PostCategoryView.as_view(), name='category-post'),
    path('category-post/<int:pk>/', views.PostCategoryView.as_view(), name='category-post'),
    path('post/new', views.post_new, name='blog-post-new'),
]