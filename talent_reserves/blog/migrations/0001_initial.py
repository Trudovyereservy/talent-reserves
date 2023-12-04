# Generated by Django 4.2.7 on 2023-12-03 11:35

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
                ('name', models.CharField(max_length=254, unique=True, verbose_name='tag')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
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
                ('image', models.ImageField(blank=True, upload_to='posts/')),
                ('tags', models.ManyToManyField(to='blog.tag', verbose_name='tag')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-publication_date'],
            },
        ),
    ]