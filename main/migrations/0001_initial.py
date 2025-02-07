# Generated by Django 5.0.2 on 2024-05-12 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='author/')),
                ('birth', models.DateField()),
                ('birth_place', models.CharField(max_length=255)),
                ('death', models.DateField(blank=True, null=True)),
                ('death_place', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField()),
                ('work', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='category/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('year', models.DateField()),
                ('pages', models.IntegerField()),
                ('publisher', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='book-image/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('has_audio', models.BooleanField()),
                ('audio_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('has_electron', models.BooleanField()),
                ('electron_types', models.TextField(blank=True, null=True)),
                ('electron_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, unique=True)),
                ('quote', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, unique=True)),
                ('body', models.TextField()),
                ('mark', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
