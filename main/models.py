from django.db import models
from django.utils import timezone


class Kalibration(models.Model):
    dateKalib = models.DateField('Дата калибровки', default=timezone.now)
    konstant = models.CharField('Текущая константа', max_length=9)
    dateKalibNext = models.DateField('Следующая дата калибровки')

    class Meta:
        verbose_name = 'Калибровка'
        verbose_name_plural = 'Калибровки'

class Viscosimetrs(models.Model):
    diameter = models.CharField('Диаметр', max_length=5)
    serialNumber = models.CharField('Заводской номер', max_length=30)
    konstant = models.ForeignKey(Kalibration, on_delete=models.CASCADE)
    Viscosity1000 = models.CharField('За 1000 сек, сСт', max_length=30)
    dateKalib = models.DateField ('Дата калибровки', default=timezone.now)
    datePov = models.DateField('Дата поверки')
    datePovDedlain = models.DateField('Дата окончания поверки')
    range = models.CharField('Диаметр', max_length=30)

    class Meta:
        verbose_name = 'Вискозиметр'
        verbose_name_plural = 'Вискозиметры'









