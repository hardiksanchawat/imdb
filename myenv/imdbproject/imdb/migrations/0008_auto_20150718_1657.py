# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0007_auto_20150718_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='genre',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=241, null=True, verbose_name=b'Genre', choices=[(b'Action', b'action'), (b'Adult', b'adult'), (b'Adventure', b'adventure'), (b'Animation', b'animation'), (b'Biography', b'biography'), (b'Comedy', b'comedy'), (b'Crime', b'crime'), (b'Documentary', b'documentary'), (b'Drama', b'drama'), (b'Family', b'family'), (b'Fantasy', b'fantasy'), (b'Film-Noir', b'film-Noir'), (b'Game-Show', b'game-Show'), (b'Historical', b'historical'), (b'Historical Fiction', b'historical Fiction'), (b'Horror', b'horror'), (b'Music', b'music'), (b'Musical', b'musical'), (b'Mystery', b'mystery'), (b'News', b'news'), (b'Reality-TV', b'reality-TV'), (b'Romance', b'romance'), (b'Sci-Fi', b'sci-Fi'), (b'Short', b'short'), (b'Sport', b'sport'), (b'Talk-Show', b'talk-Show'), (b'Thriller', b'thriller'), (b'War', b'war'), (b'Western', b'western')]),
        ),
    ]
