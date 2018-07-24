# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-11 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0009_mainpage_bottom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentpage',
            name='yandex_widget_1',
        ),
        migrations.RemoveField(
            model_name='paymentpage',
            name='yandex_widget_2',
        ),
        migrations.AddField(
            model_name='mainpage',
            name='about',
            field=models.TextField(default='', verbose_name='о журнале'),
            preserve_default=False,
        ),
    ]
