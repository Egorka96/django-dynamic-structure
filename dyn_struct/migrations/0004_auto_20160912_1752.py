# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dyn_struct', '0003_auto_20160906_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dynamicstructurefield',
            options={'ordering': ('row', 'position'), 'verbose_name': 'поле динамической структуры', 'verbose_name_plural': 'поля динамических структур'},
        ),
        migrations.AddField(
            model_name='dynamicstructure',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dynamicstructure',
            name='is_deprecated',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='dynamicstructure',
            name='version',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
        migrations.AddField(
            model_name='dynamicstructurefield',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dynamicstructure',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterUniqueTogether(
            name='dynamicstructure',
            unique_together=set([('name', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='dynamicstructurefield',
            unique_together=set([('structure', 'name', 'header')]),
        ),
    ]