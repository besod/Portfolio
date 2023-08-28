from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/',views.projects, name='projects'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    path('<int:id>/', views.blog_detail, name= 'blog_detail'),
]