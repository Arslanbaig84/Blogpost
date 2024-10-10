from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # To Do
            return redirect('/')
    form = CustomUserCreationForm
    return render(request, 'users/register.html', {'form':form})