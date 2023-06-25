from django.urls import path
from . import views

urlpatterns = [
    path('', views.story, name='story'),
    path('latest/', views.latest_stories, name='latest_stories'),
    path('<int:pk>/', views.story_detail, name='story_detail'),
    path('chapter/<int:pk>/', views.chapter_detail, name='chapter_detail'),
]
