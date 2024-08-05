from django.shortcuts import render, get_object_or_404
from .models import Doctor

# Create your views here.
def doctors_list(request):
    doctors = Doctor.objects.all().order_by('-date')
    return render(request, 'Doctors/doctors_list.html', { 'doctors': doctors })

def doctor_page(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)
    return render(request, 'Doctors/doctor_page.html', {'doctor': doctor})