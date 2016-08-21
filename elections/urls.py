from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>.+)/$', views.areas),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
]
