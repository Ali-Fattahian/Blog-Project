from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
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

 