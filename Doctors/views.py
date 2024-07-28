from django.shortcuts import render
from .models import Doctor

# Create your views here.
def doctors_list(request):
    doctors = Doctor.objects.all().order_by('-date')
    return render(request, 'doctors/doctors_list.html', { 'doctors': doctors })