from sqlite3 import connect
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutor, Tutor_infor
# Create your views here.
# def login(request):
#     return render(request, "templates/te,plate.html")

def testing(request):
  mydata = Tutor.objects.all()
#   mydata2=Tutor_infor.objects.all()
  return render(request, 'teach/course.html', {"Tutor":mydata})

# def enrolla(request):
#   if request.user.is_authenticated:
#     return render(request, "enroll/enroll.html", context = {"enroll":Tutor.objects.all, })

def enrolla(request):
    if request.user.is_authenticated:
        return render(request, "enroll/enroll.html", context = {"En":Tutor.objects.all})

  # sql = "SELECT * FROM Tutor"
  # mdata= Tutor.objects.get(id=1)
  # # data=mdata[0]
 
  # # print(mdata)
  # return render(request, 'enroll/enroll.html',{'En':mdata})

  