from django.urls import path
from . import views


app_name = 'Doctors'
urlpatterns = [
    path('', views.doctors_list, name='list'),
    path('<slug:slug>/', views.doctor_page, name='page'),
]