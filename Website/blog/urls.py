from django.urls import path
from . import views

urlpatterns = [
    path('', views.LatestPostsView.as_view(), name = 'homepage'), 
    path('posts', views.AllPostsView.as_view(), name = 'posts'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name = 'post'),
    path('read-later', views.ReadLaterView.as_view(), name = 'read-later')
]