from django.db import models
import secrets
# Create your models here.


class Course(models.Model):
    course_id = models.CharField(max_length=25, primary_key=True)
    course_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    no_of_students = models.CharField(max_length=5)
    max_no_of_students = models.CharField(max_length=5)
    duration = models.CharField(max_length=3)
    course_description = models.TextField(max_length=800)
    trainer = models.CharField(max_length=50, null=True)
    image = models.FileField(default="")

    def setCourseId(self):
        self.course_id = secrets.token_hex(8)
        return self.course_id

    def __str__(self):
        return self.course_id + '--' + self.course_name + '--' + self.trainer


class ClassroomSession(models.Model):
    session_id = models.CharField(max_length=10, primary_key=True)
    course_id = models.CharField(max_length=25)
    session_name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=2)

    def setSessionId(self):
        self.session_id = secrets.token_hex(8)
        return self.session_id

    def __str__(self):
        return self.session_name + '--' + self.duration

