from django.db import models
from talent_reserves.yandex_s3_storage import ClientMediaStorage


class Post(models.Model):
    """Model of posts"""
    text = models.TextField()
    short_description = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True, db_index=True)
    tags = models.ManyToManyField('Tag', through='TagPost')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publication_date']
        verbose_name_plural = 'posts'
        verbose_name = 'post'

    def __str__(self):
        return self.text[:15]


class Tag(models.Model):
    """Model of tags"""

    name = models.CharField(
        max_length=254,
        unique=True,
    )
    slug = models.SlugField(
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name


class TagPost(models.Model):
    """Model for connecting Tag and Post"""

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContentPost(models.Model):
    """Model of content for posts."""
    post = models.ForeignKey(
        Post,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='posts/',
        storage=ClientMediaStorage(),
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'content_post'
        verbose_name_plural = 'content_posts'
