from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomerUserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from followers.models import Follow



# Create your views here.
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email = email).exists():
            messages.info(request, 'User already exists with this email.')
            return redirect('register')
        
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # To Do
            return redirect('/')
    form = CustomUserCreationForm
    return render(request, 'users/register.html', {'form':form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Successful.")
            #To Do
            return redirect('/')

    return render(request, 'users/login_user.html')


@login_required(login_url="/users/login_user/")
def logout_user(request):
    logout(request)
    messages.info(request, 'Logged Out')
    return redirect('login_user')


@login_required(login_url="/users/login_user/")
def profile(request):
    return render(request, 'users/profile.html')


@login_required(login_url="/users/login_user/")
def userprofile(request, username):
    # Get the user whose profile is being viewed
    user_p = get_object_or_404(User, username=username)
    
    # Check if the current logged-in user follows this user
    is_followed = Follow.objects.filter(followed_by=request.user, following=user_p).exists()

    # Get the total number of posts by the user
    total_posts = Post.objects.filter(author__username=username).count()

    # Prepare the context
    user_profile = {
        'user_p': user_p,
        'total_posts': total_posts,
        'is_followed': is_followed  # Pass the follow status to the template
    }

    return render(request, 'users/userprofile.html', {'user_profile': user_profile})


def edit_profile(request):
    if request.method == 'POST':
        form = CustomerUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            print(form.errors)

    form = CustomerUserChangeForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form':form})
