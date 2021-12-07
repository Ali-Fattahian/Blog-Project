from django.shortcuts import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from blog.models import Comment, Post, Tag
from .serializers import CommentSerializer, PostSerializer, TagSerializer
from blog.utils import IsAllowedToChangePost, IsAllowedToCreatePost


@api_view(['GET',])
def main_api_page(request):
    posts_route = reverse('post-list-api', request=request)
    tags_route = reverse('tag-list-api', request=request)
    available_routes = [
        {'List of all the posts': posts_route},
        {'List of all the tags': tags_route},
    ]
    return Response(available_routes)

class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-date_created')
    serializer_class = PostSerializer
    permission_classes = [IsAllowedToCreatePost]

    # def create(self, request, *args, **kwargs):
    #     post = Post.objects.create(title=request.data['title'], excerpt=request.data['excerpt'], image=request.data['image'], content=request.data['content'], author=request.user)
    #     post.save()

    #     for tag in request.data['tag']:
    #         tag_obj = Tag.objects.get(caption=tag['caption'])
    #         post.tag.add(tag_obj)

    #     serializer = PostSerializer(post)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=HTTP_201_CREATED, headers=headers) 
    # Due to security issues
        

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


class TagListAPI(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAllowedToCreatePost]


class TagDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAllowedToCreatePost]
