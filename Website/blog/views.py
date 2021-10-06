from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from .utils import search_posts


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

# class AllPostsView(ListView): #Max Approach - this one is better for all of posts - so i use this one instead
#     template_name = 'blog/all-posts.html'
#     model = Post
#     ordering = ['-date']
#     context_object_name = 'all_posts'

def all_posts(request):
    search_query, posts = search_posts(request)
    context = {'all_posts':posts, 'search_query':search_query}
    return render(request, 'blog/all-posts.html', context)







# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug = slug)
#     # identified_post = next(post for post in all_posts if post['slug'] == slug)
#     return render(request, 'blog/post-detail.html', {
#         'one_post' : identified_post,
#         'post_tags':identified_post.tag.all()
#     })

class PostDetailView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = get_object_or_404(Post, slug = slug)
        context = {
            'one_post':post,
            'post_tags':post.tag.all(),
            'form':CommentForm(),
            'comments':post.comments.all().order_by('-id'),
            'saved_for_later':self.is_stored_post(request, post.id)
        }
        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug = slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post', args=[slug]))
        else:
            context = {
            'one_post':post,
            'post_tags':post.tag.all(),
            'form':form,
            'comments':post.comments.all().order_by('-id')
            }
            return render(request, 'blog/post-detail.html', context)
    
class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")