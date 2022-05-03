from django.shortcuts import render
from django.http  import HttpResponse

def home(request):
    news = [
        {
            'date': 1,
            'Наименование': 'ВЖ-1',
            'Партия': 4,
            'Температура': 20,
            'Термостатирование': 'да'
        },
        {
            'date': 21,
            'Наименование': 'ВЖ-2',
            'Партия': 5,
            'Температура': 50,
            'Термостатирование': 'да',
        }
    ]
    data = {'news': news,
             'title': 'Лабораторные журналы'
             }
    return render(request, 'main/home.html', data)

def production(request):
    return HttpResponse('<h3>Журналы приготовления</h3>')

def attestation(request):
    return HttpResponse('<h3>Журналы аттестации</h3>')

