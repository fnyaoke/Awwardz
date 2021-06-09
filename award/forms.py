from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'biography', 'image']

class ProjectForm(forms.ModelForm):

    class Meta:
        model= Projects
        exclude= ['author', 'created_date', 'author_profile']

class ImageForm(forms.ModelForm):
    class Meta:
        model= Projects
        exclude= ['title', 'created_date', 'country', 'author', 'author_profile']