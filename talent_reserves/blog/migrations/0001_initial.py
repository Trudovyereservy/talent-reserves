# Generated by Django 4.2.7 on 2023-11-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True, verbose_name='Название тега')),
                ('slug', models.SlugField(unique=True, verbose_name='Уникальный слаг')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('short_description', models.CharField(max_length=255)),
                ('publication_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('image', models.ImageField(blank=True, upload_to='posts/', verbose_name='Изображение')),
                ('tags', models.ManyToManyField(to='blog.tag', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-publication_date'],
            },
        ),
    ]
