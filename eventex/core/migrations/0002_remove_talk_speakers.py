# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-28 04:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='speakers',
        ),
    ]
