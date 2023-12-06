# Generated by Django 4.2.7 on 2023-12-05 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('date_published', models.DateTimeField(blank=True, help_text='Дата и время публикации (с отсрочкой)', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ('-date_published',),
            },
        ),
        migrations.CreateModel(
            name='ContentNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo_news/')),
                ('title_photo', models.CharField(blank=True, max_length=120, null=True)),
                ('author_photo', models.CharField(blank=True, max_length=50, null=True)),
                ('date_photo', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='news.news')),
            ],
            options={
                'verbose_name': 'ContentNews',
                'verbose_name_plural': 'ContentNews',
            },
        ),
    ]
