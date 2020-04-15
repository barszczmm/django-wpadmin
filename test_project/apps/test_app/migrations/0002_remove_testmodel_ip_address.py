# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='ip_address',
        ),
    ]
