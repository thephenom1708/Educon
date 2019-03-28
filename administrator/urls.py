from django.conf.urls import url, include
from . import views

app_name = 'administrator'

urlpatterns = [
    url(r'^adminPortal/$', views.adminPortal, name="adminPortal"),
    url(r'^studentApproval/$', views.studentApproval, name="studentApproval"),
    url(r'^approve/(?P<request_id>[0-9a-z]+)/$', views.approve, name="approve"),
    url(r'^deny/(?P<request_id>[0-9a-z]+)/$', views.deny, name='deny'),
]