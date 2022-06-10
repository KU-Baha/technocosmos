from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class SpaceObject(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=1500)
    area = models.CharField('Площадь', max_length=50)
    mass = models.CharField('Масса', max_length=50)
    author = models.CharField('Автор', max_length=100, null=True, blank=True)
    video_url = models.URLField('Ссылка на видео', null=True, blank=True)
    image = CloudinaryField('Изображение')
    type = models.CharField('Тип', choices=settings.SPACE_OBJECT_TYPE, max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Небесное тело'
        verbose_name_plural = 'Небесные тела'


class Status(models.Model):
    name = models.CharField('Статус', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Mission(models.Model):
    title = models.CharField('Название', max_length=50)
    space_object = models.ForeignKey(SpaceObject, on_delete=models.CASCADE, verbose_name='Планета')
    description = models.TextField('Описание', max_length=1500)
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.DO_NOTHING)
    start_date = models.DateField('Дата начала миссии')
    end_date = models.DateField('Дата окончания миссии')
    video_url = models.URLField('Ссылка на видео', null=True, blank=True)
    image = CloudinaryField('Изображение')

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
    video_url = models.URLField('Ссылка на видео', null=True, blank=True)
    image = CloudinaryField('Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'


class Gallery(models.Model):
    image = CloudinaryField('Изображение', blank=False)
    space_object = models.ForeignKey(SpaceObject, verbose_name='Небесное тело', on_delete=models.DO_NOTHING, null=True,
                                     blank=True)
    mission = models.ForeignKey(Mission, verbose_name='Миссия', on_delete=models.DO_NOTHING, null=True, blank=True)
    technology = models.ForeignKey(Technology, verbose_name='Технология', on_delete=models.DO_NOTHING, null=True,
                                   blank=True)
