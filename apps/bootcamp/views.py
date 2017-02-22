from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context= {
    "courses": Course.objects.all()
    #select all from course
    }
    return render(request, 'bootcamp/index.html', context)

def process(request):
    #using ORM (we are adding/creating a new course, description and date added)
    Course.objects.create(name = request.POST['course_name'], description = request.POST['description'])
    return redirect ('/')

def removecourse(request, id):
    context = {
    "course": Course.objects.get(id=id)
    }
    return render(request, 'bootcamp/removecourse.html', context)

def remove(request, id):
    remove_this = Course.objects.get(id=id)
    remove_this.delete()
    return redirect('/')
