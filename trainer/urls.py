from django.conf.urls import url, include
from . import views

app_name = 'trainer'

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^addCourse/$', views.addCourse, name='addCourse'),
    url(r'^(?P<course_id>[0-9a-z]+)/$', views.courseInfo, name='courseInfo')
]