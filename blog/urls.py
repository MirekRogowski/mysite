from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('user/<username>', views.UserPostListView.as_view(), name='post-users'),
    path('post/<pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post-add/', views.AddPostView.as_view(), name='post-add'),
    path('post-update/<int:pk>', views.UpdatePostView.as_view(), name='post-update'),
    path('post-delete/<int:pk>', views.DeletePostView.as_view(), name='post-delete'),
    path('post-list', views.PostAuthorizedView.as_view(), name='post-list'),
    path('category-add/', views.AddCategoryView.as_view(), name='category-add'),
    # path('category-post/<str:category>/', views.post_category_view, name='category-post'),
    path('category-post/<category>/', views.PostCategoryView.as_view(), name='category-post'),
    path('newsletter/', views.AddNewsLetterView.as_view(), name='newsletter'),
    path('post-send/<int:pk>', views.NewsLetterPostView.as_view(), name='post-send'),
    # path('post-send/<int:pk>', views.mail_letter, name='post-send'),

]

