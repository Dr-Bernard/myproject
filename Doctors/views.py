from django.shortcuts import render

# Create your views here.
def Doctors_list(request):
    return render(request, 'Doctors/Doctors_list.html')