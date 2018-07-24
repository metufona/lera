# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0002_auto_20170501_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actualarticles',
            name='number_1',
        ),
        migrations.RemoveField(
            model_name='actualarticles',
            name='number_2',
        ),
        migrations.RemoveField(
            model_name='actualarticles',
            name='number_3',
        ),
        migrations.AddField(
            model_name='actualarticles',
            name='link_1',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ссылка статиьи 1'),
        ),
        migrations.AddField(
            model_name='actualarticles',
            name='link_2',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ссылка статиьи 2'),
        ),
        migrations.AddField(
            model_name='actualarticles',
            name='link_3',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ссылка статиьи 3'),
        ),
    ]
