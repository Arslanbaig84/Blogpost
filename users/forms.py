from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

"""
class CustomerUserChangeForm(UserChangeForm):
#    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude password from being displayed or edited
        self.fields['password'].widget = forms.HiddenInput()
    
    def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
        raise forms.ValidationError("A user with that username already exists.")
    return username
"""