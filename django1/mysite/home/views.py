from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable':"this is a variable sent "
    }
    # return HttpResponse("this is homepage")
    return render(request,'index.html',context)

def about(request):
    # return HttpResponse("this is about")1
    return render(request,'about.html')

def services(request):
    # return HttpResponse("this is services")
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        no = request.POST.get('no')
        contact=Contact(name=name,email=email,no=no,date=datetime.today())
        contact.save()
        messages.success(request,'Your form has been submited')
    return render(request,'contact.html')
    
