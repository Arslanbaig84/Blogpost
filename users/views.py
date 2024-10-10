from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


# Create your views here.
def register(request):
    form = CustomUserCreationForm
    return render(request, 'users/register.html', {'form':form})