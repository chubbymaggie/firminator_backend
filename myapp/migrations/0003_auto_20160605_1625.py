# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160605_1625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authgrouppermissions',
            options={'managed': False},
        ),
    ]
