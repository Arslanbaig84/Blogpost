from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from followers.models import Follow


# Create your views here.
@login_required(login_url="/users/login_user/")
def posts(request):
    following = list(
                Follow.objects.filter(followed_by=request.user).values_list('following', flat=True)
            )
    if not following:
        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'posts/index.html', {'posts':posts})
    else:
        posts = Post.objects.filter(author__in=following).order_by('-created_at')[0:60]
        return render(request, 'posts/index.html', {'posts':posts})



@login_required(login_url="/users/login_user/")
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            article = form.cleaned_data['article']
            author = request.user
            Post.objects.create(title=title, article=article, author=author)
            messages.success(request, 'New Post added successfully.')
            return redirect('/posts/')
    form = PostForm()
    return render(request, 'posts/new_post.html', {'form':form})


@login_required(login_url="/users/login_user/")
def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post.html', {'post':post})