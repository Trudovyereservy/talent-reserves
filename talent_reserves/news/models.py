from django.db import models


class News(models.Model):
    """
    Модель для хранения новостей.
    """
    title = models.CharField(
        max_length=120
        )
    content = models.TextField()
    date_published = models.DateTimeField(
        auto_now_add=True, db_index=True
        )

    class Meta:
        ordering = ('date_published',)
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
        upload_to='photos_news/'
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

    class Meta:
        verbose_name = 'ContentNews'
        verbose_name_plural = 'ContentNews'

    def __str__(self):
        return self.news.title
