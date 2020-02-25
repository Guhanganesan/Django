from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader 

from .models import Student

def hello(request):
    return HttpResponse("<h2> Welcome!!!</h2>")
"""
def index(request):
    return HttpResponse("<h2> Index Page </h2>")
"""
def index(request):
    data={ "appname":"Dajango", "x":"How Are You!!","y":100,
           "List":[1,2,3,4,5,6]
         } 
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render(data))


def about(request):
    temp=loader.get_template('about.html')
    return HttpResponse(temp.render())

def sports(request):
    temp=loader.get_template('sports.html')
    return HttpResponse(temp.render())

def library(request):
    temp=loader.get_template('library.html')
    return HttpResponse(temp.render())


def articles(request,name,date,month,year):
    data={"articles_name":name,"date":date,"month":month,"year":year}
    temp=loader.get_template('articles.html')
    return HttpResponse(temp.render(data))

def stdData(request):
    obj1=Student()
    obj1.name="Anbu"
    obj1.id=1001
    obj1.age=28
    obj1.email="anbu@gmail.com"

    obj2=Student()
    obj2.name="Raja"
    obj2.id=1002
    obj2.age=28
    obj2.email="raja@gmail.com"

    obj3=Student()
    obj3.name="Suresh"
    obj3.id=1003
    obj3.age=28
    obj3.email="suresh@gmail.com"

    L=[obj1, obj2, obj3]
    temp=loader.get_template('student.html')
    return HttpResponse(temp.render({'listofdata':L}))







