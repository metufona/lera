# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-18 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0011_paymentpage_yandex_widget_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentpage',
            name='yandex_widget_2',
            field=models.TextField(default='', verbose_name='Виджет - Оплата оформления статьи'),
            preserve_default=False,
        ),
    ]