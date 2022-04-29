from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ViscosityMJL(models.Model):
    date = models.DateField('Дата', default=timezone.now)
    name = models.CharField('Наименование', max_length=100)
    lot = models.CharField('Партия', max_length=100)
    temperature = models.DecimalField('Температура, ℃', max_digits=5, decimal_places=2)
    termostatition = models.BooleanField('Термостатировано не менее 20 минут')
    temperatureCheck = models.BooleanField('Температура контролируется внешним поверенным термометром')
    termometer = models.CharField('Внутренний номер термометра', max_length=10)
    ViscosimeterNumber1 = models.CharField('Заводской номер вискозиметра № 1', max_length=10)
    Konstant1 = models.FloatField('Константа вискозиметра № 1')
    ViscosimeterNumber2 = models.CharField('Заводской номер вискозиметра № 1', max_length=10)
    Konstant2 = models.FloatField('Константа вискозиметра № 2')
    plustimemin11 = models.FloatField('Время истечения 11, + мин')
    plustimesek11 = models.DecimalField('Время истечения 11, + cек', max_digits=5, decimal_places=2)
    plustimemin21 = models.FloatField('Время истечения 21, + мин')
    plustimesek21 = models.DecimalField('Время истечения 21, + cек', max_digits=5, decimal_places=2)
    plustimemin12 = models.FloatField('Время истечения 12, + мин')
    plustimesek12 = models.DecimalField('Время истечения 12, + cек', max_digits=5, decimal_places=2)
    plustimemin22 = models.FloatField('Время истечения 22, + мин')
    plustimesek22 = models.DecimalField('Время истечения 22, + cек', max_digits=5, decimal_places=2)
    performer = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'проба: {self.name}, п.: {self.lot}, t℃: {self.temperature}, дата: {self.date}'