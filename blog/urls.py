from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog_index, name='blog_index'),
    path('', views.blog_home, name='blog_home'),
    path('<str:slug>/', views.blog_detail, name='blog_detail'),
    path('categoria/<category>/', views.blog_category, name='blog_category'),
]
