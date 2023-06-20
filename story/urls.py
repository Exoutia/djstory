from django.urls import path
from . import views

urlpatterns = [
    path('', views.story, name='story'),
    path('<int:pk>/', views.story_detail, name='story_detail')
]
