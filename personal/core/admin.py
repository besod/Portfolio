from django.contrib import admin
from .models import About, Project, Post
# Register your models here.


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ['name','publish']
    list_filter = ['status','created','publish']
    search_fields = ['name', 'body']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
   

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
  
   
    list_display=['title', 'slug','author','publish','status']
    list_filter = ['status','created','publish','author']
    search_fields = ['title', 'description']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    prepopulated_fields = {'slug':('title',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','publish','status']
    list_filter = ['status','created','publish','author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

