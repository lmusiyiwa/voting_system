from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vote/', views.cast_vote, name='cast_vote'),
    path('results/', views.results, name='results'),
]
