from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts':posts})


def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post.html', {'post':post})