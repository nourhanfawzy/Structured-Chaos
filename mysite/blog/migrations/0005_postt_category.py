# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150222_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='postt',
            name='category',
            field=models.TextField(default=b'Other'),
            preserve_default=True,
        ),
    ]
