from django.urls import path,reverse
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('newproject/', views.new_project, name='newproject'),
    path('search_results/', views.search_project, name="search_project"),
    path('update/', views.update_profile, name="profileupdate"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/', views.profile_info, name='profile'),
    path('accounts/register', views.registration, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

def get_success_url(self):
    return reverse('award:profile')