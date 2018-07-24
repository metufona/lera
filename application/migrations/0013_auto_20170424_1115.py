# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20170424_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='magazine_title',
            field=models.CharField(help_text='Используются для вывода выходных данных и отображения в списке статей при просмотре номера журнала', max_length=300, verbose_name='Название статьи (Rus)'),
        ),
    ]
