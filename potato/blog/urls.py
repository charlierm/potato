from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

#Import views
from views import *

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^posts/(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),
    url(r'^manage/$', AdminPostListView.as_view(), name='admin_posts'),
    url(r'^manage/posts/create/$', AdminPostCreateView.as_view(), name='admin_posts_create')

                       )