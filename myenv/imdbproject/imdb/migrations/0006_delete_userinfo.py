# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0005_auto_20150717_1904'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Userinfo',
        ),
    ]
