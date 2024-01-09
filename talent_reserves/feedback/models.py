from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ваше имя')
    email = models.EmailField(verbose_name='Ваш e-mail')
    subject = models.CharField(
        max_length=50,
        verbose_name='Тема сообщения (кратко)'
        )
    message = models.TextField(verbose_name='Ваше сообщение')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
