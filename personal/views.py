from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'personal/home.html')

def about(request):
    return HttpResponse("this is about page")

def contact(request):
    return HttpResponse("this is contact page")

def skills(request):
    return HttpResponse("this is skills page")
