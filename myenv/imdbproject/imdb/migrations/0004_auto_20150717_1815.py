# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0003_auto_20150717_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email', blank=True)),
                ('username', models.CharField(max_length=20, verbose_name=b'User Name')),
                ('password', models.CharField(max_length=20, verbose_name=b'Password')),
                ('repassword', models.CharField(max_length=20, verbose_name=b'Retype')),
            ],
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='director',
            field=models.CharField(max_length=100, verbose_name=b'Director'),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='genre',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=86, null=True, verbose_name=b'Genre', choices=[(b'ac', b'Action'), (b'au', b'Adult'), (b'ad', b'Adventure'), (b'an', b'Animation'), (b'bi', b'Biography'), (b'co', b'Comedy'), (b'cr', b'Crime'), (b'do', b'Documentary'), (b'dr', b'Drama'), (b'fa', b'Family'), (b'ft', b'Fantasy'), (b'fn', b'Film-Noir'), (b'ga', b'Game-Show'), (b'hi', b'Historical'), (b'hf', b'Historical Fiction'), (b'hr', b'Horror'), (b'ms', b'Musical'), (b'mu', b'Musical'), (b'my', b'Mystery'), (b'ne', b'News'), (b're', b'Reality-TV'), (b'ro', b'Romance'), (b'sc', b'Sci-Fi'), (b'sh', b'Short'), (b'sp', b'Sport'), (b'ta', b'Talk-Show'), (b'th', b'Thriller'), (b'wa', b'War'), (b'we', b'Western')]),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='popularity',
            field=models.FloatField(verbose_name=b'Popularity', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='score',
            field=models.FloatField(verbose_name=b'Score', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
    ]
