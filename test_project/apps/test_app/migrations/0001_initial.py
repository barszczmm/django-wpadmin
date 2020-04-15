# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('big_integer', models.BigIntegerField()),
                ('binary', models.BinaryField()),
                ('boolean', models.BooleanField(default=False)),
                ('char', models.CharField(max_length=255)),
                ('comma_separated_integer', models.CommaSeparatedIntegerField(max_length=255)),
                ('date', models.DateField()),
                ('date_time', models.DateTimeField()),
                ('decimal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('email', models.EmailField(max_length=254)),
                ('file_path', models.FilePathField(path=b'/cygdrive/c/Users/barszcz/projekty/moje/django/django-wpadmin/test_project/../docs', recursive=True)),
                ('float', models.FloatField()),
                ('integer', models.IntegerField()),
                ('ip_address', models.IPAddressField()),
                ('generic_ip_address', models.GenericIPAddressField()),
                ('null_boolean', models.NullBooleanField()),
                ('positive_integer', models.PositiveIntegerField()),
                ('positive_small_integer', models.PositiveSmallIntegerField()),
                ('slug', models.SlugField()),
                ('small_integer', models.SmallIntegerField()),
                ('text', models.TextField()),
                ('time', models.TimeField()),
                ('url', models.URLField()),
                ('foreign_key', models.ForeignKey(to='books.Book')),
                ('many_to_many', models.ManyToManyField(to='authors.Author')),
                ('one_to_one', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
