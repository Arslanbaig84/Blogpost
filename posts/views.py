from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/index.html', {'posts':posts})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            article = form.cleaned_data['article']
            Post.objects.create(title=title, article=article)
            messages.success(request, 'New Post added successfully.')
            return redirect('/posts/')
    form = PostForm()
    return render(request, 'posts/new_post.html', {'form':form})


def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post.html', {'post':post})