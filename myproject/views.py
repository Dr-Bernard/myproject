from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to your reliable Telemedicine application")

def about(request):
    return HttpResponse("About MEDTECH a subsidiary of VENTURE TRIBE")
