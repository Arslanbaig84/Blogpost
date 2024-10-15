from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Follow

@login_required(login_url="/users/login_user/")
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    
    # Check if the user is trying to follow themselves
    if request.user != user_to_follow:
        # Check if the follow relationship already exists
        if not Follow.objects.filter(followed_by=request.user, following=user_to_follow).exists():
            Follow.objects.create(followed_by=request.user, following=user_to_follow)

    return redirect(reverse('userprofile', args=[username]))


@login_required(login_url="/users/login_user/")
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    
    # Check if the follow relationship exists
    follow_relation = Follow.objects.filter(followed_by=request.user, following=user_to_unfollow).first()
    if follow_relation:
        follow_relation.delete()

    return redirect(reverse('userprofile', args=[username]))
