from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm


class ProjectUpload(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'description', 'link')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
