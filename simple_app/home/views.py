from django.shortcuts import render

# Create your views here.

def index(request):
    context={'name':"Angel",
             'age':20,
             'course':['math','physics']
        

             }
    return render(request, 'home/home.html',context)

def service(request):
    return render(request, 'home/service.html')