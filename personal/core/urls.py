from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/',views.project, name='project'),
    path('<int:id>/<slug:slug>/', views.projects_detail, name='projects_detail'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    path('<int:id>/', views.blog_detail, name= 'blog_detail'),
    path('search/', views.post_search, name='search'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)