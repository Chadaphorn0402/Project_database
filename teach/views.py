from sqlite3 import connect
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutor, Tutor_infor

# Create your views here.
# def login(request):
#     return render(request, "templates/te,plate.html")

def testing(request):
  mydata1 = Tutor.objects.get(id=1)
  mydata2 = Tutor.objects.get(id=2)
  # mydata3 = Tutor.objects.get(id=3)
  # mydata4 = Tutor.objects.get(id=4)
  # mydata5 = Tutor.objects.get(id=5)
  return render(request, 'teach/course.html', {"Tutor":mydata1,"Tutor1":mydata2})
  # ,"Tutor2":mydata3,"Tutor3":mydata4,"Tutor4":mydata5})


def enrolla(request):
    if request.user.is_authenticated:
        return render(request, "enroll/enroll.html", context = {"En":Tutor.objects.get(id=1)})

def enrolla1(request):
    if request.user.is_authenticated:
        return render(request, "enroll/enroll2.html", context = {"En1":Tutor.objects.get(id=2)})
      
# def enrolla2(request):
#     if request.user.is_authenticated:
#         return render(request, "enroll/enroll3.html", context = {"En2":Tutor.objects.get(id=3)})

# def enrolla3(request):
#     if request.user.is_authenticated:
#         return render(request, "enroll/enroll4.html", context = {"En3":Tutor.objects.get(id=4)})

# def enrolla4(request):
#     if request.user.is_authenticated:
#         return render(request, "enroll/enroll5.html", context = {"En4":Tutor.objects.get(id=5)})

def enrollmentt(request):
    if request.user.is_authenticated:
        return render(request, "enrollment/enrollment.html", context = {"Enment":Tutor.objects.all})

  # sql = "SELECT * FROM Tutor"
  # mdata= Tutor.objects.get(id=1)
  # # data=mdata[0]
 
  # # print(mdata)
  # return render(request, 'enroll/enroll.html',{'En':mdata})
