import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import hashlib, secrets
from .models import User, Student
from trainer.models import Course


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
        context = {
            'user': new_user,
            'page': 'dashboard',
            'courses': courses
        }
        if new_user.type == 'student':
            return render(request, 'studentPortal.html', context)
        elif new_user.type == 'trainer':
            return render(request, 'trainerPortal.html', context)
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        sha = hashlib.sha256()
        sha.update(password.encode('utf-8'))
        password_hash = sha.hexdigest()

        user = User.objects.filter(username=username, password_hash=password_hash) or None

        if user is None:
            context = {
                'error_msg': 'Invalid Credentials! Please try again!'
            }
            return render(request, 'login.html', context)
        else:
            request.session['type'] = user[0].type
            request.session['username'] = user[0].username

            courses = Course.objects.filter(trainer=user[0].username)
            context = {
                'user': user[0],
                'page': 'dashboard',
                'courses': courses
            }
            if user[0].type == 'student':
                return render(request, 'studentPortal.html', context)
            elif user[0].type == 'trainer':
                return render(request, 'trainerPortal.html', context)
    return render(request, 'index.html')


def logout(request):
    request.session['type'] = None
    request.session['username'] = None
    return render(request, 'index.html')
