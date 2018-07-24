# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='magazine',
            options={'ordering': ('year', 'mouth'), 'verbose_name': 'Выпуск журнала', 'verbose_name_plural': 'Выпуски журнала'},
        ),
        migrations.AddField(
            model_name='magazine',
            name='mouth',
            field=models.IntegerField(choices=[(1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')], default=1, verbose_name='Месяц'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magazine',
            name='year',
            field=models.IntegerField(default=1, verbose_name='Год'),
            preserve_default=False,
        ),
    ]
