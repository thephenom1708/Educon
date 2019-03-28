from django.shortcuts import render, get_object_or_404
from auth.models import User, Student
from .models import Course, ClassroomSession, Content
from student.models import StudentCourse
# Create your views here.


def getLoggedInUser(request):
    username = request.session['username']
    user = User.objects.filter(username=username)
    return user[0]


def dashboard(request):
    user = getLoggedInUser(request)
    totalStudents = Student.objects.count()
    totalCourses = Course.objects.count()
    totalSessions = ClassroomSession.objects.count()
    totalTrainers = User.objects.filter(type='trainer').count()

    courses = Course.objects.filter(trainer=user.username)
    context = {
        'user': user,
        'page': 'dashboard',
        'courses': courses,
        'totalStudents': totalStudents,
        'totalCourses': totalCourses,
        'totalSessions': totalSessions,
        'totalTrainers': totalTrainers
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

        totalStudents = Student.objects.count()
        totalCourses = Course.objects.count()
        totalSessions = ClassroomSession.objects.count()
        totalTrainers = User.objects.filter(type='trainer').count()

        context = {
            'user': user,
            'page': 'dashboard',
            'courses': courses,
            'totalStudents': totalStudents,
            'totalCourses': totalCourses,
            'totalSessions': totalSessions,
            'totalTrainers': totalTrainers
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
    classroom_sessions = ClassroomSession.objects.filter(course_id=course_id)
    mapped_students = StudentCourse.objects.filter(course_id=course_id)
    contents = Content.objects.filter(course_id=course_id)

    enrolled_students = []

    for student in mapped_students:
        stu = Student.objects.filter(username=student.username)
        if len(stu) != 0:
            enrolled_students.append(stu[0])

    if course_id is not None:
        course = get_object_or_404(Course, pk=course_id)
        context = {
            'user': user,
            'course': course,
            'classroom_sessions': classroom_sessions,
            'enrolled_students': enrolled_students,
            'contents': contents
        }
        return render(request, 'trainerCourseInfo.html', context)


def createSession(request, course_id):
    user = getLoggedInUser(request)

    if request.method == "POST":
        session = ClassroomSession()
        session.session_name = request.POST['name']
        session.duration = request.POST['duration']
        session.course_id = course_id
        session.session_id = session.setSessionId()
        session.save()

        context = {
            'user': user,
            'session': session
        }
        return render(request, 'trainerVideoConference.html', context)


def shareContent(request, course_id):
    user = getLoggedInUser(request)
    classroom_sessions = ClassroomSession.objects.filter(course_id=course_id)
    mapped_students = StudentCourse.objects.filter(course_id=course_id)

    enrolled_students = []

    for student in mapped_students:
        stu = Student.objects.filter(username=student.username)
        if len(stu) != 0:
            enrolled_students.append(stu[0])

    if request.method == "POST" and request.FILES['file']:
        newContent = Content()
        newContent.content_name = request.POST['name']
        newContent.content_file = request.FILES.get('file', None)
        newContent.course_id = course_id

        newContent.save()
        contents = Content.objects.filter(course_id=course_id)
    if course_id is not None:
        course = get_object_or_404(Course, pk=course_id)

        context = {
            'user': user,
            'course': course,
            'classroom_sessions': classroom_sessions,
            'enrolled_students': enrolled_students,
            'contents': contents
        }
        return render(request, 'trainerCourseInfo.html', context)


