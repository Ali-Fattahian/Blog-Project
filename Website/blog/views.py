from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def posts(request):
    pass

def post_detail(request):
    pass