from django.db import models


class Tag(models.Model):
    """Модель тегов в блоге."""

    name = models.CharField(
        max_length=254,
        unique=True,
        verbose_name='Название тега',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальный слаг',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Post(models.Model):
    """Модель постов в блоге."""
    text = models.TextField()
    short_description = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True, db_index=True)
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
    )
    # Доработать поле image с учетом хранилища S3
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        ordering = ['-publication_date']
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

    def __str__(self):
        return self.text[:15]
