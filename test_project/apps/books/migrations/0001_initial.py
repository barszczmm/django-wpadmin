# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('publication_date', models.DateField(verbose_name='publication date')),
                ('author', models.ForeignKey(verbose_name='author', to='authors.Author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
            ],
            options={
                'verbose_name': 'Category of Books',
                'verbose_name_plural': 'Categories of Books',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(verbose_name='category', to='books.BookCategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(verbose_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
