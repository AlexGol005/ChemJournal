from django.shortcuts import render
from django.http  import HttpResponse

def home(request):
    return HttpResponse('<h3>Журналы приготовления и аттестации</h3>')

def production(request):
    return HttpResponse('<h3>Журналы приготовления</h3>')

def attestation(request):
    return HttpResponse('<h3>Журналы аттестации</h3>')

def VG(request):
    table = [
        {
        'date': 1,
        'Наименование': 'СО',
        'Партия': 4,
        'Температура': 20,
        'Термостатирование': 'да'
        },
        {
            'date': 21,
            'Наименование': 'СО2',
            'Партия': 5,
            'Температура': 50,
            'Термостатирование': 'да',
        }
    ]
    listg = {'table': table,
             'title': 'Определение кинематической вязкости'
    }

    return render(request, 'main/VG.html', listg)

def K(request):
    return render(request, 'main/K.html')