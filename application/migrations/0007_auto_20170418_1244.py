# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20170418_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='number',
            field=models.IntegerField(default=0, unique=True, verbose_name='Порядковый номер статьи'),
        ),
    ]
