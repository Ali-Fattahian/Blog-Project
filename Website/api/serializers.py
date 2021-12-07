from rest_framework import serializers
from blog.models import Post, Comment, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'caption']
        # depth = 1 


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source = 'post.title')
    author = serializers.ReadOnlyField(source = 'author.username')
    date_created = serializers.DateTimeField(read_only = True)
    class Meta:
        model = Comment
        fields = ['id', 'comment_content', 'post','author', 'date_created']


class PostSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)
    date_created = serializers.DateTimeField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    tag = TagSerializer(read_only=True, many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'excerpt', 'image', 'date', 'date_created', 'slug', 'content', 'author', 'tag', 'comments']


