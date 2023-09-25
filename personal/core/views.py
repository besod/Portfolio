from django.shortcuts import render, get_object_or_404
from .models import Post,Project,About,Status,Contact
from django.http import Http404
from .forms import ContactForm, SearchForm
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchVector
from django.core.mail import send_mail
from decouple import config
from django.conf import settings

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
    # Initialize form and query variables
    form = SearchForm()
    query = None

    # Check if there's a search query in the request
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Use SearchVector to perform a search on title and body fields
            posts = Post.published.annotate(
                search=SearchVector('title', 'body'),
            ).filter(search=query)
    else:
        # If no search query, display all published blog posts
        posts = Post.published.all()

    return render(request, 'blog.html', {
        'posts': posts,
        'form': form,
        'query': query,
    })

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
           
           # Send a notification email to personal email address
            subject = cd['subject']
            message = f'Name: {cd["name"]}\nEmail: {cd["email"]}\nSubject: {cd["subject"]}\nMessage: {cd["message"]}'
            from_email = cd['email']
            recipient = [config('EMAIL_HOST_USER')]  

            send_mail(subject, message, from_email, recipient)

            #save message in DB
            Contact.objects.create(
                name=cd['name'],
                email=cd['email'],
                subject=['subject'],
                message=cd['message'])
            sent = True

            return render(request, 'emailsent.html')
    else:
        form = ContactForm()  # Create an empty form for GET requests

    return render(request, 'contact.html', {'form': form, 'sent': sent})


