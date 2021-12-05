from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('posts/', views.PostListAPI.as_view(), name='post-list-api'),
    path('posts/<slug:slug>', views.PostDetailAPI.as_view(), name='post-detail-api'),
]
