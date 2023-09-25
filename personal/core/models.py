from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Status.PUBLISHED)
class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

class About(models.Model):
    name = models.CharField(max_length=50)    
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    github = models.URLField(max_length=250,blank=True, null=True)
    linkedin = models.URLField(max_length=250,blank=True, null=True)
    twitter = models.URLField(max_length=250,blank=True, null=True)
    facebook = models.URLField(max_length=250,blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['-publish']),]
    
    def __str__(self) :
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    technology = models.CharField(max_length=250)
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    links = models.TextField(max_length=250,blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects',default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    publish = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    published = PublishedManager() #custom manager overriding default manager above

    class Meta:
        ordering = ['title']
        indexes = [models.Index(fields=['-publish']),]
       
    def __str__(self):
        return self.title
    

class Post(models.Model):    
    
    title = models.CharField(max_length=250)
    slug= models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    links = models.URLField(max_length=250, blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager() #custom manager overriding default manager above


    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100, null=False)    
    email = models.EmailField(max_length=254, null=False)
    subject = models.TextField(default=True)
    message = models.TextField(null=False)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

