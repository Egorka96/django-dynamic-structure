# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 10:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dyn_struct', '0004_auto_20160912_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dynamicstructurefield',
            options={'ordering': ('structure__name', 'row', 'position'), 'verbose_name': 'поле динамической структуры', 'verbose_name_plural': 'поля динамических структур'},
        ),
    ]