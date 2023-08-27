from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def projects(request):
    return render(request, 'projects.html',{})

def blog(request):
    posts = Post.published.all()
    return render(request, 'blog.html',{'posts':posts})

def blog_detail(request, id):
    post = get_object_or_404(Post, id=id,status=Post.Status.PUBLISHED)
    
    return render(request, 'blog_detail.html',{'post':post})

def contact(request):
    return render(request, 'contact.html',{})

