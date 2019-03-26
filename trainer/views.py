from django.shortcuts import render, get_object_or_404
from auth.models import User, Student
from .models import Course
# Create your views here.


def getLoggedInUser(request):
    username = request.session['username']
    user = User.objects.filter(username=username)
    return user[0]


def dashboard(request):
    user = getLoggedInUser(request)
    courses = Course.objects.filter(trainer=user.username)
    context = {
        'user': user,
        'page': 'dashboard',
        'courses': courses
    }
    return render(request, 'trainerPortal.html', context)


def addCourse(request):
    user = getLoggedInUser(request)
    courses = Course.objects.filter(trainer=user.username)

    if request.method == "POST" and request.FILES['image']:
        newCourse = Course()
        newCourse.image = request.FILES['image']
        newCourse.course_name = request.POST['name']
        newCourse.category = request.POST['category']
        newCourse.max_no_of_students = request.POST['maxStudents']
        newCourse.no_of_students = '0'
        newCourse.duration = request.POST['duration']
        newCourse.course_description = request.POST['description']
        newCourse.trainer = request.POST.get('trainer', None)

        newCourse.course_id = newCourse.setCourseId()
        newCourse.save()
        context = {
            'user': user,
            'page': 'dashboard',
            'courses': courses
        }
        return render(request, 'trainerPortal.html', context)
    else:
        context = {
            'user': user,
            'page': 'addCourse'
        }
        return render(request, 'addCourse.html', context)


def courseInfo(request, course_id):
    user = getLoggedInUser(request)

    if course_id is not None:
        course = get_object_or_404(Course, pk=course_id)
        context = {
            'user': user,
            'course': course
        }
        return render(request, 'courseInfo.html', context)

