from django.http import HttpResponse
from django.shortcuts import render
from .models import School, Student

# Create your views here.


def school_detail(request, school_id):

    school_info = School.objects.get(id=school_id)

    context = {
        'school': school_info
    }

    return render(request, 'education/school_detail.html', context)


def school_list(request):
    school_details = School.objects.all()

    context = {
        'schools': school_details
    }

    return render(request, 'education/school_list.html', context)


def student_list(request):

    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'education/student_list.html', context)


def student_detail(request, student_id):

    student = Student.objects.get(id=student_id)

    print(student.author.name)

    context = {
        'student': student
    }

    return render(request, 'education/student_detail.html', context)

