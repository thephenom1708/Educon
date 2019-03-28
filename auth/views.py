import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import hashlib, secrets
from .models import User, Student
from trainer.models import Course, ClassroomSession
from student.models import StudentCourse


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        new_user = User()
        new_user.username = request.POST['username']
        new_user.email = request.POST['email']
        new_user.type = request.POST['type']
        password = request.POST['password']

        sha = hashlib.sha256()
        sha.update(password.encode('utf-8'))
        password_hash = sha.hexdigest()
        new_user.password_hash = password_hash

        new_user.save()
        request.session['type'] = new_user.type
        request.session['username'] = new_user.username

        courses = Course.objects.filter(trainer=new_user.username)

        totalStudents = Student.objects.count()
        totalCourses = Course.objects.count()
        totalSessions = ClassroomSession.objects.count()
        totalTrainers = User.objects.filter(type='trainer').count()

        if new_user.type == 'student':
            context = {
                'user': new_user,
                'page': 'dashboard'
            }
            return render(request, 'profile.html', context)

        elif new_user.type == 'trainer':
            context = {
                'user': new_user,
                'page': 'dashboard',
                'courses': courses,
                'totalStudents': totalStudents,
                'totalTrainers': totalTrainers,
                'totalCourses': totalCourses,
                'totalSessions': totalSessions,

            }
            return render(request, 'trainerPortal.html', context)
        elif new_user.type == 'admin':
            students = Student.objects.all()
            context = {
                'user': new_user,
                'page': 'dashboard',
                'students': students,
                'totalStudents': totalStudents,
                'totalTrainers': totalTrainers,
            }
            return render(request, 'adminPortal.html', context)
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        sha = hashlib.sha256()
        sha.update(password.encode('utf-8'))
        password_hash = sha.hexdigest()

        user = User.objects.filter(username=username, password_hash=password_hash) or None

        if len(user) == 0:
            context = {
                'error_msg': 'Invalid Credentials! Please try again!'
            }
            return render(request, 'login.html', context)
        else:
            totalStudents = Student.objects.count()
            totalCourses = Course.objects.count()
            totalSessions = ClassroomSession.objects.count()
            totalTrainers = User.objects.filter(type='trainer').count()

            request.session['type'] = user[0].type
            request.session['username'] = user[0].username

            courses = Course.objects.filter(trainer=user[0].username)

            if user[0].type == 'student':

                opted_mapped_courses = StudentCourse.objects.filter(username=user[0].username, approved=True)
                opted_courses = []

                for course in opted_mapped_courses:
                    c = Course.objects.filter(course_id=course.course_id)
                    opted_courses.append(c[0])

                context = {
                    'user': user[0],
                    'page': 'dashboard',
                    'courses': opted_courses,
                    'totalStudents': totalStudents,
                    'totalCourses': totalCourses,
                    'totalSessions': totalSessions,
                    'totalTrainers': totalTrainers
                }

                return render(request, 'studentPortal.html', context)

            elif user[0].type == 'trainer':
                context = {
                    'user': user[0],
                    'page': 'dashboard',
                    'courses': courses,
                    'totalStudents': totalStudents,
                    'totalCourses': totalCourses,
                    'totalSessions': totalSessions,
                    'totalTrainers': totalTrainers
                }
                return render(request, 'trainerPortal.html', context)

            elif user[0].type == 'admin':
                students = Student.objects.all()
                context = {
                    'user': user[0],
                    'page': 'dashboard',
                    'students': students,
                    'totalStudents': totalStudents,
                    'totalTrainers': totalTrainers,
                }
                return render(request, 'adminPortal.html', context)
    return render(request, 'login.html')


def logout(request):
    request.session['type'] = None
    request.session['username'] = None
    return render(request, 'index.html')
