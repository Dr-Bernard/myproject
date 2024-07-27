from django.shortcuts import render
from .models import Doctors

# Create your views here.
def Doctors_list(request):
    doctors = Doctors.objects.all()
    return render(request, 'Doctors/Doctors_list.html', { 'Doctors': Doctors })