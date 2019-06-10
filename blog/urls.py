from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<str:slug>/', views.blog_detail, name='blog_detail'),
    path('<category>/', views.blog_category, name='blog_category'),
]