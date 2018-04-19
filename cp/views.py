from django.shortcuts import render, render_to_response

# Create your views here.
from cp.models import Student


def showRealStudents(request):
    list = Student.objects.all()
    return render_to_response('student.html', {'students': list})