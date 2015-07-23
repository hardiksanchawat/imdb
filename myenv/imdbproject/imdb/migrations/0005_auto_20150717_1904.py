# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0004_auto_20150717_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=32, verbose_name=b'Password'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='repassword',
            field=models.CharField(max_length=32, verbose_name=b'Retype Password'),
        ),
    ]
