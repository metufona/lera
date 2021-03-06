# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0016_auto_20170426_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='specialmagazine',
            name='example',
            field=models.TextField(blank=True, help_text='Отображается на странице журнала', null=True, verbose_name='Пример выходных данных'),
        ),
        migrations.AlterField(
            model_name='specialmagazine',
            name='number',
            field=models.CharField(help_text='Используется для ссылки: 9 -> S9', max_length=300, unique=True, verbose_name='Номер журнала'),
        ),
        migrations.AlterField(
            model_name='specialmagazine',
            name='organizator',
            field=models.TextField(blank=True, help_text='Отображается на странице журнала', null=True, verbose_name='Организатор'),
        ),
        migrations.AlterField(
            model_name='specialmagazine',
            name='title',
            field=models.CharField(max_length=300, unique=True, verbose_name='Заголовок журнала'),
        ),
    ]
