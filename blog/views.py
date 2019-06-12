from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    paginator = Paginator(posts, 12)  # number posts for page 
    page = request.GET.get('page')
    posts = paginator.get_page(page)  # page where post is 
    context = {
        'posts' : posts,
        'blog' : 'active',
    }
    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains = category).order_by('-created_on')
    context = {
        'posts' : posts,
        'category' : category,
        'blog' : 'active',
    }
    return render(request, 'blog_category.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)  # if post doesn't exist return error404
    comments = Comment.objects.filter(post=post)

    # comment form
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post,
            )
            comment.save()
            return HttpResponseRedirect('/' + slug)  # when a comment is sent, user is redirect to the same page but with empyt form 

    context = {
        'post' : post,
        'comments' : comments,
        'form' : form,
        'blog' : 'active',
    }
    return render(request, 'blog_detail.html', context)

