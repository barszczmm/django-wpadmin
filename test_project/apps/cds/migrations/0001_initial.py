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
            name='Cd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('author', models.ForeignKey(verbose_name='author', to='authors.Author')),
            ],
            options={
                'verbose_name': 'CD',
                'verbose_name_plural': 'CDs',
            },
        ),
        migrations.CreateModel(
            name='CdCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
            ],
            options={
                'verbose_name': 'Category of CDs',
                'verbose_name_plural': 'Categories of CDs',
            },
        ),
        migrations.AddField(
            model_name='cd',
            name='category',
            field=models.ForeignKey(verbose_name='category', to='cds.CdCategory'),
        ),
        migrations.AddField(
            model_name='cd',
            name='owner',
            field=models.ForeignKey(verbose_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
