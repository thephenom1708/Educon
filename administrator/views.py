from django.shortcuts import render, get_object_or_404
from auth.models import User,Student
from student.models import StudentCourse


def getLoggedInUser(request):
    username = request.session['username']
    user = User.objects.filter(username=username)
    return user[0]


def adminPortal(request):
    user = getLoggedInUser(request)
    totalStudents = Student.objects.count()
    totalTrainers = User.objects.filter(type='trainer').count()
    students=Student.objects.all()

    context={
        'user': user,
        'page': 'dashboard',
        'students':students,
        'totalStudents': totalStudents,
        'totalTrainers': totalTrainers
    }
    return render(request, 'adminPortal.html', context)


def studentApproval(request):
    user = getLoggedInUser(request)
    approval_requests = StudentCourse.objects.filter(approved=False)

    context = {
        'user': user,
        'page': 'studentApproval',
        'approval_requests': approval_requests,
        'totalRequests': len(approval_requests)
    }
    return render(request, 'studentApproval.html', context)


def approve(request, request_id):
    user = getLoggedInUser(request)

    approval_request = StudentCourse.objects.get(id=request_id)
    approval_request.approved = True
    approval_request.save(update_fields=['approved'])

    x = studentApproval(request)
    return x


def deny(request, request_id):
    user = getLoggedInUser(request)

    approval_request = StudentCourse.objects.filter(id=request_id).delete()

    x = studentApproval(request)
    return x

