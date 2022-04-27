from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index1.html')
def add(request):
    name = request.GET.get('name')
    password = request.GET.get('PWD')
    address = request.GET.get('address')
    city = request.GET.get('city')
    gender = request.GET.get('gender')
    vehicle = request.GET.getlist('vehicle')
    dob = request.GET.get('dob')
    salary = request.GET.get('salary')

    return render(request, 'result.html',
                  {'city': city, 'gender': gender, 'dob': dob, 'vehicle': vehicle, 'address': address, 'name': name,
                   'password': password, 'salary': salary})


#def home(abc):
   # return HttpResponse("<h1>hello maneesh</h1>")

