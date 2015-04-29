# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linkid', models.CharField(max_length=5)),
                ('link', models.URLField()),
                ('created', models.DateTimeField(verbose_name=b'Created Date')),
            ],
        ),
    ]
