# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odetta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='data_urls',
            field=models.TextField(blank=True),
        ),
    ]
