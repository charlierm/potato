from django.conf.urls import patterns, include, url

#Import views
from views import IndexView, DetailView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),
                       )