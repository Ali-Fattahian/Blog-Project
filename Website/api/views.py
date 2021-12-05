from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from blog.models import Comment, Post
from .serializers import CommentSerializer, PostSerializer
from blog.utils import IsAllowedToChangePost, IsAllowedToCreatePost


class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAllowedToCreatePost]


    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAllowedToChangePost]
    lookup_field = 'slug'


class CommentListAPI(generics.ListCreateAPIView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        return Comment.objects.filter(post=post)
        
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        serializer.save(author=self.request.user, post=post)
 

class CommentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        return Comment.objects.filter(post=post)

    serializer_class = CommentSerializer
    permission_classes = [IsAllowedToChangePost]
