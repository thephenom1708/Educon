from django.db import models
import secrets
# Create your models here.


class StudentCourse(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    username = models.CharField(max_length=100)
    course_id = models.CharField(max_length=25)
    approved = models.BooleanField(default=False)

    def setId(self):
        self.id = secrets.token_hex(8)
        return self.id

    def __str__(self):
        return self.username + '--' + self.course_id + '--' + str(self.approved)

