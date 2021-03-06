# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_article_magazine_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AlterField(
            model_name='article',
            name='annotation_end',
            field=models.TextField(default='', verbose_name='Аннотация (Eng)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='annotation_rus',
            field=models.TextField(default='', verbose_name='Аннотация (Rus)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.CharField(blank=True, help_text='Авторы при отображении статьи (Фамилия Имя Отчество полностью)', max_length=300, null=True, verbose_name='Авторы'),
        ),
        migrations.AlterField(
            model_name='article',
            name='magazine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Magazine', verbose_name='Выпуск журнала'),
        ),
        migrations.AlterField(
            model_name='article',
            name='magazine_authors',
            field=models.CharField(help_text='(Фамилия И.О.) Используются для вывода выходных данных и отображения в списке статей при просмотре номера журнала', max_length=300, verbose_name='Авторы в журнале'),
        ),
        migrations.AlterField(
            model_name='article',
            name='magazine_title',
            field=models.CharField(blank=True, help_text='Используются для вывода выходных данных и отображения в списке статей при просмотре номера журнала', max_length=300, null=True, verbose_name='Заголовок в журнале'),
        ),
        migrations.AlterField(
            model_name='article',
            name='number',
            field=models.IntegerField(help_text='Используется для ссылки: 1 -> article0001', unique=True, verbose_name='Порядковый номер статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pages',
            field=models.CharField(blank=True, help_text='Используются для вывода выходных данных', max_length=300, null=True, verbose_name='Страницы в журнале'),
        ),
        migrations.AlterField(
            model_name='article',
            name='science',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Science', verbose_name='Вид наук'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_eng',
            field=models.CharField(help_text='Заголовок (на английском языке) при отображении статьи', max_length=300, verbose_name='Название статьи (Eng)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(help_text='Ссылка на Google Drive', max_length=300, verbose_name='Cсылка'),
        ),
    ]
