from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import  static


urlpatterns=[
    url(r'^$', views.index, name='home'),
    url(r'^$', views.index, name='home'),
    url(r'^api/merch/$', views.LoginView.as_view()),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$', views.MerchDescription.as_view()),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    url(r'^profile/$', views.profile_info, name='profile'),
    url(r'^update/$', views.profile_update, name='update'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^new_post/', views.new_post, name = 'new_post'),
    url(r'^add_image/', views.add_image, name = 'add_image'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)