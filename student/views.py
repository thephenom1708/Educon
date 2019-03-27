from django.shortcuts import render, get_object_or_404
from auth.models import User, Student
from trainer.models import Course, ClassroomSession
from .models import StudentCourse
# Create your views here.


def getLoggedInUser(request):
    username = request.session['username']
    user = User.objects.filter(username=username)
    return user[0]


def dashboard(request):
    user = getLoggedInUser(request)
    opted_mapped_courses = StudentCourse.objects.filter(username=user.username)
    courses = []

    for course in opted_mapped_courses:
        c = Course.objects.filter(course_id=course.course_id)
        courses.append(c[0])
    print(courses)

    context = {
        'user': user,
        'page': 'dashboard',
        'courses': courses
    }
    return render(request, 'studentPortal.html', context)


def viewCourses(request):
    user = getLoggedInUser(request)
    courses = Course.objects.all()

    context = {
        'user': user,
        'courses': courses,
        'page': 'viewCourses'
    }
    return render(request, 'viewCourses.html', context)


def courseInfo(request, course_id):
    user = getLoggedInUser(request)
    classroom_sessions = ClassroomSession.objects.filter(course_id=course_id)

    if course_id is not None:
        course = get_object_or_404(Course, pk=course_id)
        context = {
            'user': user,
            'course': course,
            'classroom_sessions': classroom_sessions,
        }
        return render(request, 'courseInfo.html', context)


def registerCourseInfo(request, course_id):
    user = getLoggedInUser(request)

    if course_id is not None:
        course = get_object_or_404(Course, pk=course_id)
        context = {
            'user': user,
            'course': course,
        }
        return render(request, 'registerCourseInfo.html', context)


def registerCourse(request, course_id):
    user = getLoggedInUser(request)
    courses = Course.objects.all()

    if course_id is not None:
        newStudentCourse = StudentCourse()
        newStudentCourse.course_id = course_id
        newStudentCourse.username = user.username

        newStudentCourse.id = newStudentCourse.setId()
        newStudentCourse.save()

        context = {
            'user':user,
            'msg': 'The Enrollment approval request has been sent to Course Admin Successfully !!!',
            'courses': courses,
            'page': 'viewCourses'
        }
        return render(request, 'viewCourses.html', context)
