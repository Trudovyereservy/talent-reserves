from django.db import models


class Tag(models.Model):
    """Model of tags"""

    name = models.CharField(
        max_length=254,
        unique=True,
        verbose_name='tag',
    )
    slug = models.SlugField(
        unique=True,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name


class Post(models.Model):
    """Model of posts"""
    text = models.TextField()
    short_description = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True, db_index=True)
    tags = models.ManyToManyField(
        Tag,
        verbose_name='tag',
    )
    # Доработать поле image с учетом хранилища S3
    image = models.ImageField(
        upload_to='posts/',
        blank=True
    )

    class Meta:
        ordering = ['-publication_date']
        verbose_name_plural = 'posts'
        verbose_name = 'post'

    def __str__(self):
        return self.text[:15]
