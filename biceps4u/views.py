from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from biceps4u.models import contactus
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request, 'index.html',context)
    #return HttpResponse("This Is Homepage")
def aboutus(request):
    return render(request, 'aboutus.html')
    #return HttpResponse("This Is About us Page")
def workouts(request):
    return render(request, 'workouts.html')
    #return HttpResponse("This Is workout Page")
def gallary(request):
    return render(request, 'gallary.html')
    #return HttpResponse("This Is gallary Page")
def packages(request):
    return render(request, 'packages.html')
def social(request):
    return render(request, 'social.html')
    #return HttpResponse("This Is social Page")
def contactus(request):
    if request.method =='POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        queries = request.POST.get('queries')
        contact = contactus(name=name,phone=phone,email=email,queries=queries,date=datetime.today())
        contact.save()
        messages.success(request,'Your Contact Has Been Shared With Us, We Will Get Back To You Soon')

    return render(request, 'contactus.html')
    #return HttpResponse("This Is contactus Page")`