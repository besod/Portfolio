from django.shortcuts import render, get_object_or_404
from .models import Post,Project,About,Status,Contact
from django.http import Http404
from .forms import ContactForm
from django.core.mail import send_mail

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
    sent = False  # Initialize the 'sent' variable to False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form field passed validation
            cd = form.cleaned_data
            Contact.objects.create(
                name=cd['name'],
                email=cd['email'],
                message=cd['message']
            )

            sent = True
            return render(request, 'emailsent.html')
    else:
        form = ContactForm()  # Create an empty form for GET requests

    return render(request, 'contact.html', {'form': form, 'sent': sent})


