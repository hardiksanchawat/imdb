# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0006_delete_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='genre',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=93, null=True, verbose_name=b'Genre', choices=[(b'ac', b'Action'), (b'au', b'Adult'), (b'Adventure', b'adventure'), (b'an', b'Animation'), (b'bi', b'Biography'), (b'co', b'Comedy'), (b'cr', b'Crime'), (b'do', b'Documentary'), (b'dr', b'Drama'), (b'fa', b'Family'), (b'ft', b'Fantasy'), (b'fn', b'Film-Noir'), (b'ga', b'Game-Show'), (b'hi', b'Historical'), (b'hf', b'Historical Fiction'), (b'hr', b'Horror'), (b'ms', b'Musical'), (b'mu', b'Musical'), (b'my', b'Mystery'), (b'ne', b'News'), (b're', b'Reality-TV'), (b'ro', b'Romance'), (b'sc', b'Sci-Fi'), (b'sh', b'Short'), (b'sp', b'Sport'), (b'ta', b'Talk-Show'), (b'th', b'Thriller'), (b'wa', b'War'), (b'we', b'Western')]),
        ),
    ]
