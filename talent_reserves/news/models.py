from django.db import models
from blog.models import Tag


class News(models.Model):
    """
    Модель для хранения новостей.
    """
    title = models.CharField(
        max_length=120
        )
    description = models.TextField()
    tags = models.ManyToManyField('blog.Tag', through='TagNews')
    date_published = models.DateTimeField(
        help_text='Дата и время публикации (с отсрочкой)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_published',)
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class ContentNews(models.Model):
    """
    Модель для хранения новостного контента,
    связанного с определенной новостью.
    """
    news = models.ForeignKey(
        News,
        related_name='images',
        on_delete=models.CASCADE
        )
    image = models.ImageField(
        upload_to='photo_news/'
        )
    title_photo = models.CharField(
        max_length=120,
        blank=True, null=True,
        )
    author_photo = models.CharField(
        max_length=50,
        blank=True, null=True
        )
    date_photo = models.DateField(
        blank=True, null=True
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ContentNews'
        verbose_name_plural = 'ContentNews'

    def __str__(self):
        return self.news.title


class TagNews(models.Model):
    """Модель для связи тегов и новостей"""

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'tag news'
        verbose_name_plural = 'tag news'
