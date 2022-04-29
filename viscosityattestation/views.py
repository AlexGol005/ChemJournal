from django.shortcuts import render
from django.http  import HttpResponse

def viscositymeasurement(request):
    return HttpResponse('<h3>Определение кинематической вязкости</h3>')