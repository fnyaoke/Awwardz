from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404, HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly



# Create your views here.
def index(request):
    date =dt.date.today()
    projects = Projects.objects.all()
    print("Projects...",projects)
    return render(request, 'index.html', locals())

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

        permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class MerchDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return MoringaMerch.objects.get(pk=pk)
        except MoringaMerch.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch)
        return Response(serializers.data)

@login_required(login_url='/accounts/login/?next=/')
def new_post(request):
        current_user = request.user
        if request.method == 'POST':
                form = ProjectForm(request.POST, request.FILES)
                if form.is_valid():
                        add=form.save(commit=False)
                        add.author = current_user
                        add.save()
                return redirect('posts/post_project.html')
        else:
                form = ProjectForm()
                return render(request,'posts/post_project.html', {"form":form})

# Create your views here.
class SignupView(FormView):
    """Signup View."""
    template_name = 'user_registration/signup.html'
#     form_class = Signup
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """If the form is valid save the user"""
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout View."""

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update a user's profile view"""
    template_name = 'django_registration/profile_update.html'
    model = Profile
    fields = ['user', 'biography', 'image']
    # Return success url
    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username_slug': username})


class UserDetailView(DetailView):
    """User detail view."""
    template_name = 'detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username_slug'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(profile__user=user).order_by('-created')
        return context


@login_required(login_url='/registration/login/')
def add_image(request):
        current_user = request.user
        if request.method == 'POST':
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                        add=form.save(commit=False)
                        add.user = current_user
                        add.save()
                return redirect('home')
        else:
                form = ImageForm()
                return render(request,'image.html', {"form":form})

@login_required(login_url='/accounts/login/')
def profile_info(request):
        current_user = request.user
        profile = Profile.objects.filter(user=current_user).first()
        # posts = request.user.images.all()

        return render(request, 'user_registration/user_profile.html', { "profile": profile})

@login_required(login_url='/accounts/login/')
def profile_update(request):
         current_user = request.user
         if request.method == 'POST':
                form = UpdateForm(request.POST, request.FILES)
                if form.is_valid():
                        add=form.save(commit=False)
                        add.user = current_user
                        add.save()
                return redirect('profile')
         else:
                form = UpdateForm()
         return render(request,'django_registration/profile_update.html',{"form":form})


@login_required(login_url='/accounts/login/')
def get_project(request, id):
    project = Projects.objects.get(pk=id)

    return render(request, 'posts/project.html', {'project':project})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username__icontains = search_term)
        message = f"{search_term}"
        profile_pic = User.objects.all()
        return render(request, 'search.html', {'message':message, 'results':searched_users, 'profile_pic':profile_pic})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message':message})

def search(request):
    profiles = User.objects.all()
    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        return render(request,'search.html',locals())
    return redirect('home')

class ProjectList(APIView):
    def get(self, request, format=None):
        allprojects = Projects.objects.all()
        serializers = ProjectsSerializer(allprojects, many=True)
        return Response(serializers.data)
        permission_classes = (IsAdminOrReadOnly)


class ProfileList(APIView):
    def get(self, request, format=None):
        allprofiles = Profile.objects.all()
        serializers = ProfileSerializer(allprofiles, many=True)
        return Response(serializers.data)
        permission_classes = (IsAdminOrReadOnly)

