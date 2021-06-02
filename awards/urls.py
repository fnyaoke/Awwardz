"""awards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.contrib import admin
from django.contrib.auth import views as auth_views
from award.views import PostViewset, ProfileViewset
from django_registration.backends.activation.views import RegistrationView
from django.conf import settings

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('award.urls')),
    path('', include(router.urls)),
    path('accounts/register', RegistrationView.as_view(success_url='/accounts/login/'), include('django_registration.backends.activation.urls')),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': settings.LOGIN_REDIRECT_URL}, name='logout'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('django.contrib.auth.urls')),

]
