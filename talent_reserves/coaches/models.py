from django.db import models
from talent_reserves.yandex_s3_storage import ClientMediaStorage

NAME_MAX_LENGTH = 64


class Direction(models.Model):
    '''
    Модель для хранения информации о направлениях работы тренеров.
    '''
    slug = models.SlugField(
        null=False,
        blank=False,
        unique=True
    )
    title = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
        unique=True
    )

    class Meta:
        ordering = ['-title']
        verbose_name = 'Direction'
        verbose_name_plural = 'Directions'

    def __str__(self) -> str:
        return f'{self.title}'


class Coach(models.Model):
    '''
    Модель для хранения информации о тренерах.
    '''
    surname = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )
    patronymic = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True
    )
    birthday = models.DateField()
    achievements = models.TextField(
        max_length=400,
        blank=True
    )
    directions = models.ManyToManyField(
        Direction,
        related_name='coaches'
    )
    photo = models.ImageField(
        upload_to='coaches/',
        storage=ClientMediaStorage(),
        null=True,
        default=None)

    class Meta:
        ordering = ['-surname']
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}'
