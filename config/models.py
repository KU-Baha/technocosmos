from django.contrib.auth.models import User
from django.db import models


class Planet(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=1500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'


class Status(models.Model):
    name = models.CharField('Статус', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Mission(models.Model):
    title = models.CharField('Название', max_length=50)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')
    description = models.TextField('Описание', max_length=1500)
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.DO_NOTHING)
    start_date = models.DateField('Дата начала миссии')
    end_date = models.DateField('Дата окончания миссии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Миссия'
        verbose_name_plural = 'Миссии'


class Technology(models.Model):
    name = models.CharField('Название', max_length=50)
    authors = models.ManyToManyField(User, verbose_name='Авторы', related_name='technology')
    description = models.TextField('Описание', max_length=1500)
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'
