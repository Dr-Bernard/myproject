# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Welcome to MEDTECH, your reliable Telemedicine application")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("About MEDTECH a subsidiary of VENTURE TRIBE")
    return render(request, 'about.html')
