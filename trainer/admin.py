from django.contrib import admin
from .models import Course, ClassroomSession, Content
# Register your models here.

admin.site.register(Course)
admin.site.register(ClassroomSession)
admin.site.register(Content)
