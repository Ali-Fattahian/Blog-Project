from django.db.models import Q
from .models import Post

def search_posts(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    posts = Post.objects.filter(Q(title__icontains = search_query) | Q(excerpt__icontains = search_query)).order_by('-date')

    return search_query, posts