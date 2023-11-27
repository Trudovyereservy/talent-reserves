from django.db import models


NAME_MAX_LENGTH = 64


class Coach(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )
    surname = models.CharField(
        max_length=NAME_MAX_LENGTH
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

    class Meta:
        ordering = ['-surname']
        verbose_name = 'Coach'
        verbose_name_plural = 'Coaches'

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}'
