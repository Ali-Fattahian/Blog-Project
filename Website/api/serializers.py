from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)
    date_created = serializers.DateTimeField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'excerpt', 'image', 'date', 'date_created', 'slug', 'content', 'author', 'tag']