from django.urls import path
from . import views

urlpatterns = [
    # path('send-letter/', views.send_letter, name='send-letter'),
    path('send-letter/', views.SendLetter.as_view(), name='send-letter'),
    path('', views.subscribers, name='subscribers'),

]