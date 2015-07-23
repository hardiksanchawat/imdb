# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0008_auto_20150718_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieinfo',
            old_name='score',
            new_name='imdb_score',
        ),
    ]
