# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20170411_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='input_data',
            field=models.TextField(blank=True, null=True, verbose_name='Входные данные'),
        ),
    ]