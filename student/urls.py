from django.conf.urls import url, include
from . import views

app_name = 'student'

urlpatterns = [
    url(r'^saveStudent/$', views.saveStudent, name='saveStudent'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^viewCourses/$', views.viewCourses, name='viewCourses'),
    url(r'^(?P<course_id>[0-9a-z]+)/$', views.courseInfo, name='courseInfo'),
    url(r'^registerCourseInfo/(?P<course_id>[0-9a-z]+)/$', views.registerCourseInfo, name='registerCourseInfo'),
    url(r'^registerCourse/(?P<course_id>[0-9a-z]+)/$', views.registerCourse, name='registerCourse'),
    url(r'^cancelEnrollment/(?P<course_id>[0-9a-z]+)/$', views.cancelEnrollment, name='cancelEnrollment'),
]