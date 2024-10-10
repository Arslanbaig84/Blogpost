from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

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


def logout_user(request):
    logout(request)
    messages.info(request, 'Logged Out')
    return redirect('login_user')
