from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import TemplateView, ListView, DetailView


def get_date(post):
    return post['date']






# def latest_posts(request):
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     return render(request, 'blog/index.html', {
#         'posts':latest_posts
#     })


class LatestPostsView(TemplateView): #My Approach
    template_name = 'blog/index.html'
    all_posts = Post.objects.all().order_by('-date')[:3]
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['posts'] = self.all_posts
        return context


# class LatestPostsView(ListView): #Max Approach
#     template_name = 'blog/index.html'
#     model = Post
#     ordering = ['date']
#     context_object_name = 'all_posts'

#     def get_queryset(self):
#         query_set =  super().get_queryset()
#         newest_data = query_set[:3] #just the first three
#         return newest_data





# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#     return render(request, 'blog/all-posts.html', {
#         'all_posts':all_posts
#     })

# class AllPostsView(TemplateView): #My Approach
#     template_name = 'blog/all-posts.html'
#     all_posts = Post.objects.all()
    
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['all_posts'] = self.all_posts
#         return context

class AllPostsView(ListView): #Max Approach - this one is better for all of posts - so i use this one instead
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'







# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug = slug)
#     # identified_post = next(post for post in all_posts if post['slug'] == slug)
#     return render(request, 'blog/post-detail.html', {
#         'one_post' : identified_post,
#         'post_tags':identified_post.tag.all()
#     })

class PostDetailView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['one_post'] = self.object
        context['post_tags'] = self.object.tag.all()
        return context
