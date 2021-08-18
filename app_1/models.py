from django.db import models
from mptt.models import MPTTModel,TreeForeignKey
# Create your models here.


class Employee(MPTTModel):
    name = models.CharField(max_length=255,unique=True,verbose_name='ФИО')
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='YUY')
    position = models.CharField(max_length=255, verbose_name='Должность')
    date = models.DateTimeField(verbose_name='Дата приема на работу')
    earnings = models.DecimalField(max_digits=12,decimal_places=4,verbose_name='Заработная плата')
    inform = models.DecimalField(max_digits=12,decimal_places=4,verbose_name='Информация о выплаченной зп')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

