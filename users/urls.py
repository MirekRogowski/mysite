from django.urls import path
from .views import UserRegisterView, BlogLoginView, UserRegister

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('', BlogLoginView.as_view(), name='login'),
    # path('register/', SignUp_Form, name='register'),
    # path('profile/', user_views.profile, name='profile'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]