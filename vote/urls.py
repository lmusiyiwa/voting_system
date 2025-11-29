# vote/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.sa_politics_news, name='sa_politics_news'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
]
