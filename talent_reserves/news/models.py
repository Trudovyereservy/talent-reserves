from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('date_published',)
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class ContentNews(models.Model):
    news = models.ForeignKey(
        News,
        related_name='images',
        on_delete=models.CASCADE
        )
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.news.title
