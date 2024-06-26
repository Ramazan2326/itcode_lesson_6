# Generated by Django 5.0.4 on 2024-05-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=5)),
                ('profile_image', models.ImageField(upload_to='profile_images')),
                ('has_oscar', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'актер',
                'verbose_name_plural': 'актеры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('genre', models.CharField(blank=True, max_length=20)),
                ('premiere', models.DateField()),
                ('description', models.TextField(blank=True, max_length=500)),
                ('poster', models.ImageField(upload_to='posters')),
            ],
            options={
                'verbose_name': 'фильм',
                'verbose_name_plural': 'фильмы',
            },
        ),
    ]
