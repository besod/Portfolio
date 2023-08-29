from django.shortcuts import render, get_object_or_404
from .models import Post,Project,About,Status
from django.http import Http404

# Create your views here.
def index(request):
    about = get_object_or_404(About, status=Status.PUBLISHED)
    return render(request, 'index.html',{'about':about})

def project(request):
    projects = Project.objects.all()
    return render(request, 'projects.html',{'projects':projects})

def projects_detail(request, id, slug):
    project = get_object_or_404(Project, id=id, slug=slug,status=Status.PUBLISHED)
    return render(request, 'projects_detail.html',{'project':project})

def blog(request):
    posts = Post.published.all()
    return render(request, 'blog.html',{'posts':posts})

def blog_detail(request, id):
    post = get_object_or_404(Post, id=id,status=Status.PUBLISHED)
    
    return render(request, 'blog_detail.html',{'post':post})

def contact(request):
    return render(request, 'contact.html',{})

