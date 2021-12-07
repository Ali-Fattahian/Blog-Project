from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_api_page, name='main-api-page'),
    path('posts/', views.PostListAPI.as_view(), name='post-list-api'),
    path('posts/<slug:slug>', views.PostDetailAPI.as_view(), name='post-detail-api'),
    path('posts/<slug:slug>/comments', views.CommentListAPI.as_view(), name='comment-list-api'),
    path('posts/<slug:slug>/comments/<int:pk>', views.CommentDetailAPI.as_view(), name='comment-detail-api'),
    path('tags', views.TagListAPI.as_view(), name='tag-list-api'),
    path('tags/<int:pk>', views.TagDetailAPI.as_view(), name='tag-detail-api'),
]
