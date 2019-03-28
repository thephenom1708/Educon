from django.shortcuts import render, get_object_or_404
from auth.models import User, Student
from trainer.models import Course, ClassroomSession, Content
from .models import StudentCourse
# Create your views here.


def getLoggedInUser(request):
    username = request.session['username']
    user = User.objects.filter(username=username)
    return user[0]


def saveStudent(request):
    if request.method == 'POST':
        new_student = Student()
        new_student.username = request.POST['username']
        new_student.email = request.POST['email']
        new_student.first_name = request.POST['firstName']
        new_student.last_name = request.POST['lastName']
        new_student.mobile = request.POST['mobile']
        new_student.education = request.POST['education']
        new_student.institute = request.POST['institute']
        new_student.city = request.POST['city']
        new_student.state = request.POST['state']
        new_student.pincode = request.POST['pincode']
        new_student.address = request.POST['address']

        new_student.save()

        x = dashboard(request)
        return x


def dashboard(request):
    totalStudents = Student.objects.count()
    totalCourses = Course.objects.count()
    totalSessions = ClassroomSession.objects.count()
    totalTrainers = User.objects.filter(type='trainer').count()
    user = getLoggedInUser(request)

    opted_mapped_courses = StudentCourse.objects.filter(username=user.username, approved=True)
    courses = []

    for course in opted_mapped_courses:
        c = Course.objects.filter(course_id=course.course_id)
        courses.append(c[0])
    print(courses)

    context = {
        'user': user,
        'page': 'dashboard',
        'courses': courses,
        'totalStudents': totalStudents,
        'totalCourses': totalCourses,
        'totalSessions': totalSessions,
        'totalTrainers': totalTrainers
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
    contents = Content.objects.filter(course_id=course_id)

    if course_id is not None:
        course = get_object_or_404(Course, pk=course_id)
        context = {
            'user': user,
            'course': course,
            'classroom_sessions': classroom_sessions,
            'contents': contents
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
    student = Student.objects.filter(username=user.username)
    courses = Course.objects.all()
    flag = 1
    if course_id is not None:
        opted_courses = StudentCourse.objects.filter(username=user.username)

        for course in opted_courses:
            if course.course_id == course_id:
                flag = 0
                break

        if flag != 0:
            course = Course.objects.filter(course_id=course_id)

            newStudentCourse = StudentCourse()
            newStudentCourse.course_id = course_id
            newStudentCourse.course_name = course[0].course_name
            newStudentCourse.username = user.username
            newStudentCourse.name = student[0].first_name + ' ' + student[0].last_name
            newStudentCourse.id = newStudentCourse.setId()
            newStudentCourse.save()

            context = {
                'user':user,
                'msg': 'The Enrollment approval request has been sent to Course Admin Successfully !!!',
                'courses': courses,
                'page': 'viewCourses',
                'flag': 1
            }
            return render(request, 'viewCourses.html', context)

        else:
            context = {
                'user': user,
                'courses': courses,
                'page': 'viewCourses',
                'msg': 'You have already enrolled for this Course !!!',
                'flag': 0
            }

            return render(request, 'viewCourses.html', context)


def cancelEnrollment(request, course_id):
    totalStudents = Student.objects.count()
    totalCourses = Course.objects.count()
    totalSessions = ClassroomSession.objects.count()
    totalTrainers = User.objects.filter(type='trainer').count()
    user = getLoggedInUser(request)

    opted_mapped_courses = StudentCourse.objects.filter(username=user.username)
    courses = []

    for course in opted_mapped_courses:
        c = Course.objects.filter(course_id=course.course_id)
        courses.append(c[0])

    StudentCourse.objects.filter(username=user.username, course_id=course_id).delete()
    context = {
        'user': user,
        'courses': courses,
        'page': 'dashboard',
        'msg': 'The course enrollment has been cancelled by you !!!',
        'totalStudents': totalStudents,
        'totalCourses': totalCourses,
        'totalSessions': totalSessions,
        'totalTrainers': totalTrainers
    }
    return render(request, 'studentPortal.html', context)


