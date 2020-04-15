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
            name='Dvd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('author', models.ForeignKey(verbose_name='author', to='authors.Author')),
            ],
            options={
                'verbose_name': 'DVD',
                'verbose_name_plural': 'DVDs',
            },
        ),
        migrations.CreateModel(
            name='DvdCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
            ],
            options={
                'verbose_name': 'Category of DVDs',
                'verbose_name_plural': 'Categories of DVDs',
            },
        ),
        migrations.AddField(
            model_name='dvd',
            name='category',
            field=models.ForeignKey(verbose_name='category', to='dvds.DvdCategory'),
        ),
        migrations.AddField(
            model_name='dvd',
            name='owner',
            field=models.ForeignKey(verbose_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
